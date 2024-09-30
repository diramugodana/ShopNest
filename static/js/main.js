// Wrap the code in a jQuery document-ready function
(function($) {

    // jQuery objects for commonly used elements
    var $window = $(window),
        $body = $('body'),
        $header = $('#header'),
        $banner = $('#banner');

    // Breakpoints definition using the breakpoints library
    breakpoints({
        wide:      ('1281px', '1680px'),
        normal:    ('981px', '1280px'),
        narrow:    ('737px', '980px'),
        narrower:  ('737px', '840px'),
        mobile:    ('481px', '736px'),
        mobilep:   (null, '480px')
    });

    // Play initial animations on page load.
    $window.on('load', function() {
        window.setTimeout(function() {
            $body.removeClass('is-preload');
        }, 100);
    });

    // Dropdowns initialization using dropotron
    $('#nav > ul').dropotron({
        alignment: 'right'
    });

    

    // Button creation
    $('<div id="navButton">' +
        '<a href="#navPanel" class="toggle"></a>' +
    '</div>').appendTo($body);

    // Panel creation
    $('<div id="navPanel">' +
        '<nav>' +
            $('#nav').navList() +
        '</nav>' +
    '</div>').appendTo($body)
    .panel({
        delay: 500,
        hideOnClick: true,
        hideOnSwipe: true,
        resetScroll: true,
        resetForms: true,
        side: 'left',
        target: $body,
        visibleClass: 'navPanel-visible'
    });

    // Header setup
    if (!browser.mobile &&
        $header.hasClass('alt') &&
        $banner.length > 0) {

        $window.on('load', function() {

            // Scrollex initialization for header animations
            $banner.scrollex({
                bottom: $header.outerHeight(),
                terminate: function() { $header.removeClass('alt'); },
                enter: function() { $header.addClass('alt reveal'); },
                leave: function() { $header.removeClass('alt'); }
            });

        });

    }

})(jQuery);
