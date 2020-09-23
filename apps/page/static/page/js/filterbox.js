window.onload = function() {

    const posts = $('#posts')[0].children

    function send_filter() {
        location.href = location.origin + '?filter=' + (String(filter).replace(',', "%2C"));
    }

    function filter_onclick(event) {
        target = event.target

        filter.splice(filter.indexOf(target.innerHTML), 1)
        
        filters_html.removeChild(target);
        tags_html.appendChild(target);

        target.onclick = tags_onclick
        send_filter()
    }

    function tags_onclick(event) {
        target = event.target

        filter.push(target.innerHTML)

        tags_html.removeChild(target);
        filters_html.appendChild(target);

        target.onclick = filter_onclick
        send_filter()
    }

    // Step 1: Get everything necessary from the DOM
    const tags = [];
    const filter = [];

    const tags_html = $('.filter-box #tags')[0]
    const filters_html = $('.filter-box #filter')[0]

    for(let index = 0; index < tags_html.children.length; index++){
        tags.push(tags_html.children[index].innerHTML);
    }

    for(let index = 0; index < filters_html.children.length; index++){
        filter.push(filters_html.children[index].innerHTML);
    }

    // Step 2: Set up onclick listeners to swap their position depending on which div they are on
    //         TAGS_HTML => FILTER and FILTER => TAGS_HTML
    for (let tag_html of tags_html.children) {
        tag_html.onclick = tags_onclick
    };

    for (let filter_html of filters_html.children) {
        filter_html.onclick = filter_onclick
    };

    // Step 3: Assign Filterbutton onclick event
    
    $('#filter-button')[0].onclick = send_filter;


}