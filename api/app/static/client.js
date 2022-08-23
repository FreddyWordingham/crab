class Client {
    // == Navigation ==
    static go_to_homepage() {
        window.location.href = "/";
    }

    // == CRUD ==
    static get_all(success, error) {
        $.ajax({
            url: "/db",
            type: "GET",
            success: success,
            error: error,
        });
    }

    static add_new(record, success, error) {
        $.ajax({
            url: "/db",
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify(record),
            success: success,
            error: error,
        });
    }
}
