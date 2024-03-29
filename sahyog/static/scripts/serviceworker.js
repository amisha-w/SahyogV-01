var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/sahyog/index/',
        '/static/style.css/',
        '/Users',
        '/adminarea',
        '/newindex.html'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/sahyog/')) {
        event.respondWith(caches.match('/sahyog/index/'));
        return;
      }
      if ((requestUrl.pathname === '/static/')) {
        event.respondWith(caches.match('/static/style.css/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});