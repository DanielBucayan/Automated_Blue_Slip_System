from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from django.core.cache import cache
import time
 
class RateLimitMiddleware(MiddlewareMixin):
    RATE_LIMIT = 50  # Number of allowed requests
    TIME_PERIOD = 60  # Time period of requests in seconds
    BLOCK_DURATION = 180  # Block duration for blocked requests
    DELAY = 2  # Minimum delay between successive requests
 
    def process_request(self, request):
        ip = self.get_client_ip(request)
        count_key = f'rate-limit-{ip}-count'
        time_key = f'rate-limit-{ip}:last_request'
        block_key = f'rate-limit-{ip}:blocked'
 
        # Check if IP is blocked
        if cache.get(block_key):
            return JsonResponse({'error': 'Rate limit exceeded. Try again later'}, status=429)
 
        # Initialize request count or increment if already exists
        request_count = cache.get_or_set(count_key, 0, timeout=self.TIME_PERIOD)
        # Apply delay if necessary
        current_time = time.time()
        last_request_time = cache.get(time_key, current_time)
        time_passed = current_time - last_request_time
 
        if time_passed < self.DELAY:
            time.sleep(self.DELAY - time_passed)
 
        # Update last request time
        cache.set(time_key, current_time, timeout=self.TIME_PERIOD)
 
        # Increment the request count
        request_count = cache.incr(count_key)
 
        # Warning if approaching the rate limit
        if request_count == 20 and request_count < self.RATE_LIMIT:
            return JsonResponse({'warning': 'You are approaching the Rate Limit'})
 
        # Block IP if rate limit exceeded
        if request_count >= self.RATE_LIMIT:
            cache.set(block_key, True, timeout=self.BLOCK_DURATION)
            return JsonResponse({'error': 'Rate limit exceeded. Try again later'}, status=429)
 
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip