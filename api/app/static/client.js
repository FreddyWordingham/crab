class Client {
    // == Navigation ==
    static go_to_homepage() {
        window.location.href = "/";
    }

    // == CRUD ==
    static get_all(collection, success, error) {
        $.ajax({
            url: "/db/" + collection,
            type: "GET",
            success: success,
            error: error,
        });
    }

    static add_new(collection, record, success, error) {
        $.ajax({
            url: "/db/" + collection,
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(record),
            success: success,
            error: error,
        });
    }
}
