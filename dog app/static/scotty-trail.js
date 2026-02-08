(function() {
    // Paw print trail behind the Scotty cursor
    var PAW_SVG = '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">' +
        '<ellipse cx="8" cy="11" rx="3.5" ry="4" fill="#C41230" opacity="0.7"/>' +
        '<ellipse cx="4" cy="5.5" rx="1.8" ry="2.2" fill="#C41230" opacity="0.7"/>' +
        '<ellipse cx="12" cy="5.5" rx="1.8" ry="2.2" fill="#C41230" opacity="0.7"/>' +
        '<ellipse cx="7" cy="3" rx="1.5" ry="2" fill="#C41230" opacity="0.7"/>' +
        '<ellipse cx="10" cy="2.5" rx="1.5" ry="2" fill="#C41230" opacity="0.7" transform="rotate(10 10 2.5)"/>' +
        '</svg>';
    var pawDataUrl = 'data:image/svg+xml;base64,' + btoa(PAW_SVG);

    var lastX = 0, lastY = 0;
    var TRAIL_DISTANCE = 50; // pixels between each paw print
    var isLeft = true; // alternate left/right paw offset

    // Inject CSS for trail elements
    var style = document.createElement('style');
    style.textContent =
        '@keyframes pawFade { 0% { opacity: 0.5; transform: scale(1); } 100% { opacity: 0; transform: scale(0.5); } }' +
        '.paw-trail { position: fixed; pointer-events: none; z-index: 9999; width: 16px; height: 16px; animation: pawFade 1.2s ease forwards; }';
    document.head.appendChild(style);

    document.addEventListener('mousemove', function(e) {
        var dx = e.clientX - lastX;
        var dy = e.clientY - lastY;
        var dist = Math.sqrt(dx * dx + dy * dy);

        if (dist >= TRAIL_DISTANCE) {
            var paw = document.createElement('img');
            paw.src = pawDataUrl;
            paw.className = 'paw-trail';

            // Offset left/right to simulate walking gait
            var offsetX = isLeft ? -8 : 8;
            var angle = Math.atan2(dy, dx);
            var perpX = Math.cos(angle + Math.PI / 2) * offsetX;
            var perpY = Math.sin(angle + Math.PI / 2) * offsetX;

            paw.style.left = (e.clientX - 8 + perpX) + 'px';
            paw.style.top = (e.clientY - 8 + perpY) + 'px';

            // Rotate paw to match movement direction
            var deg = (angle * 180 / Math.PI) + 90;
            paw.style.transform = 'rotate(' + deg + 'deg)';

            document.body.appendChild(paw);
            isLeft = !isLeft;
            lastX = e.clientX;
            lastY = e.clientY;

            // Remove after animation ends
            setTimeout(function() { paw.remove(); }, 1200);
        }
    });
})();
