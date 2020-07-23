$(document).ready(function () {
    const form0 = $("#form_buying_product");
    console.log(form0);

    function CartUpdating(product_id, num, is_delete) {
        const data = {};
        data.product_id = product_id;
        data.amount = num;
        data["csrfmiddlewaretoken"] = $("#form_buying_product [name='csrfmiddlewaretoken']").val();

        if (is_delete) {
            data["is_delete"] = true;
        }

        const url0 = form0.attr("action");
        console.log(data)
        $.ajax({
            url: url0,
            type: "POST",
            data: data,
            cache: true,
            success: function (data) {
                console.log("k");
                console.log(data.products_total_num);
                if (data.products_total_num || data.products_total_num == 0) {
                    $("#cart_total_num").text("(" + data.products_total_num + ")");
                    console.log(data.products);
                    $(".cart-items ul").html(""); // для отчистки области в случае если элемент был добавлен в корзину
                    $.each(data.products, function (k, v) {
                        $(".cart-items ul").append('<li>' + v.product_name + ", " + v.amount + "шт. " + v.price_per_item + "Rub" +
                            '<a class="delete-item" href="" data-product_id=" ' + v.id + ' "> &times; </a>' +
                            '</li>')
                    });
                }

            },
            error: function () {
                console.log("Error")
            }
        })
    }

    form0.on("submit", function (e) {
        e.preventDefault();
        console.log("receiving form");
        const num = $("#number").val();
        console.log(num);
        if(parseInt(num) > 0) {
            const submit_btn = $("#submit_btn");
            const submit = document.getElementById("submit")
            const btn = document.getElementById("submit_btn");
            const span = document.getElementsByClassName("close")[0];
            const product_id = submit_btn.data("product_id");
            const product_name = submit_btn.data("product_name");
            const product_price = submit_btn.data("product_price");
            console.log(product_id);
            console.log(product_name);
            console.log(product_price);
            //btn.onclick = function(){
            submit.style.display = "block";
            //}
            span.onclick = function(){
                submit.style.display = "none";
            }

            window.onclick = function(event){
               if (event.target === submit){
                    submit.style.display = "none";
               }
            }

            CartUpdating(product_id, num, false)


            $(".cart-items ul").append('<li>' + product_name + ", " + num + "шт. " + product_price + "Rub" +
                '</li>')
        }
        else if(parseInt(num) <= 0 || num === ""){
            const submit = document.getElementById("not-submit")
            const btn = document.getElementById("submit_btn");
            const span = document.getElementsByClassName("close")[1];
            submit.style.display = "block";

            span.onclick = function(){
                submit.style.display = "none";
            }

            window.onclick = function(event){
               if (event.target === submit){
                    submit.style.display = "none";
               }
            }
        }
    });


    $(document).ready(function () {
        const form1 = $("#form_product");
        console.log(form1);

        function CartUpdating(product_id, num, is_delete) {
            const data = {};
            data.product_id = product_id;
            data.amount = num;
            data["csrfmiddlewaretoken"] = $("#form_product [name='csrfmiddlewaretoken']").val();

            if (is_delete) {
                data["is_delete"] = true;
            }

            const url1 = form1.attr("action");
            console.log(data)
            $.ajax({
                url: url1,
                type: "POST",
                data: data,
                cache: true,
                success: function (data) {
                    console.log("k");
                    console.log(data.products_total_num);
                    if (data.products_total_num || data.products_total_num == 0) {
                        $("#cart_total_num").text("(" + data.products_total_num + ")");
                        console.log(data.products);
                        $(".cart-items ul").html(""); // для отчистки области в случае если элемент был добавлен в корзину
                        $.each(data.products, function (k, v) {
                            $(".cart-items ul").append('<li>' + v.product_name + ", " + v.amount + "шт. " + v.price_per_item + "Rub" +
                                '<a class="delete-item" href="" data-product_id=" ' + v.id + ' "> &times; </a>' +
                                '</li>')
                        });
                    }

                },
                error: function () {
                    console.log("Error")
                }
            })
        }

        form1.on("submit", function (e) {
            e.preventDefault();
            console.log("receiving form");
            const num = $("#number").val();
            console.log(num);
            if(parseInt(num) > 0) {
                const submit_btn = $("#submit_btn");
                const product_id = submit_btn.data("product_id");
                const product_name = submit_btn.data("product_name");
                const product_price = submit_btn.data("product_price");
                console.log(product_id);
                console.log(product_name);
                console.log(product_price);

                CartUpdating(product_id, num, false)


                $(".cart-items ul").append('<li>' + product_name + ", " + num + "шт. " + product_price + "Rub" +
                    '</li>')
            }
        });


        function showCart() {
            $(".cart-items").toggleClass("hidden");
        }

        $("#cart-container").on("click", function (e) {
            e.preventDefault();
            showCart()
        })

        $(".cart-container").mouseover(function () {
            showCart()
        })

        $(".cart-container").mouseout(function () {
            showCart()
        })

        $(document).on("click", ".delete-item", function (e) {
            e.preventDefault();
            product_id = $(this).data("product_id")
            num = 0;
            CartUpdating(product_id, num, true)
        })

        function CalcCartamount() {
            var total_order_amount = 0;
            $(".total-amount-in-cart").each(function () {
                total_order_amount += parseFloat($(this).text());
            })
            console.log(total_order_amount);
            $("#total_order_amount").text(total_order_amount.toFixed(2));

        }

        $(document).on("change", ".product-in-cart-amount", function () {
            let current_amount = $(this).val();
            console.log(current_amount);
            const current_tr = $(this).closest("tr");
            const current_price = parseFloat(current_tr.find(".product-price").text()).toFixed(2);
            console.log(current_price);
            const total_amount = parseFloat(current_amount * current_price).toFixed(2);
            console.log(total_amount)
            current_tr.find(".total-amount-in-cart").text(total_amount);
            CalcCartamount();

        });

        CalcCartamount();
        let inp = document.querySelector('#tel');
            // Проверяем фокус
            inp.addEventListener('focus', _ => {
                // Если там ничего нет или есть, но левое
                if(!/^\+\d*$/.test(inp.value))
                // То вставляем знак плюса как значение
                    window.onclick = function(event){
                       if (event.target === inp){
                            inp.value = "+";
                       }
                    }
            });
            inp.addEventListener('keypress', e => {
                // Отменяем ввод не цифр
                if(!/\d/.test(e.key))
                    e.preventDefault();
            });

            var old = 0;

            inp.onkeydown = function() {
                var curLen = inp.value.length;

            if (curLen < old){
                old--;
                return;
                }
                if (curLen === 2)
                    inp.value = inp.value + "(";

                if (curLen === 6)
                    inp.value = inp.value + ")-";

                if (curLen === 11)
                    inp.value = inp.value + "-";

                if (curLen === 14)
                    inp.value = inp.value + "-";

                if (curLen > 16)
                    inp.value = inp.value.substring(0, inp.value.length - 1);

                old++;
            }
    });

});

