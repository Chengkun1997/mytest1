<template>

    <div class="float-btn-group">
        <button class="btn-float btn-triger pink" @click="trigger(0)">
            <i class="icon-bars"></i>
        </button>
        <div class="btn-list">
            <!-- <a href="#" class="btn-float "><i class="fa fa-search"></i></a>
            <a href="#" class="btn-float "><i class="fa fa-cloud-download"> </i></a>
            <a href="#" class="btn-float "><i class="fa fa-paperclip"> </i></a>
            <a href="#" class="btn-float "><i class="fa fa-line-chart"> </i></a> -->
            <a href="#" class="btn-float "><img src="../assets/img/Icon/bought.png" style="width:30px;height:30px"></a>
            <a href="#" class="btn-float "><img src="../assets/img/Icon/bought.png" style="width:30px;height:30px"></a>
            <a href="#" class="btn-float "><img src="../assets/img/Icon/bought.png" style="width:30px;height:30px"></a>
            <a href="#" class="btn-float "><img src="../assets/img/Icon/bought.png" style="width:30px;height:30px"></a>
            <a href="#" class="btn-float "><img src="../assets/img/Icon/bought.png" style="width:30px;height:30px"></a>
        </div>
    </div>

</template>
<script>
    // import $ from "../assets/js/jquery-2.1.1.min.js"
    // window.jQuery = $;
    // window.$ = $;
    export default {
        name: "Demo2sample",
        methods: {
            trigger(num) {
                // $(this).closest(".float-btn-group").toggleClass("open")
                // document.querySelector('.float-btn-group').classList.toggle('open');
                document.querySelectorAll(".float-btn-group")[num].classList.toggle("open");
            },
        },
        mounted() {
            // var btnTriger = document.getElementsByClassName(".btn-triger")
            // btnTriger.click(function () {
            //     $(this).closest(".float-btn-group").toggleClass("open");
            // });
            console.log(document.querySelector(".float-btn-group"));
            console.log(document.querySelectorAll(".float-btn-group"));
        },
    };
</script>


<style scoped>
    /* @import "../assets/css/htmleaf-demo.css";
    @import "../assets/css/normalize.css"; */
    /* @import "../assets/css/default.css"; */
    @import "../assets/css/stylesDemo2.css";
    /* @import "http://cdn.bootcss.com/font-awesome/4.4.0/css/font-awesome.min.css"; */
</style>