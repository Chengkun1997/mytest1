<template>
    <article class="htmleaf-container">
        <section class="model-1">
            <div class="float-btn-group">
                <button class="btn-float btn-triger pink" @click="trigger(0)">
                    <i class="icon-bars"></i>
                </button>
                <div class="btn-list">
                    <a href="#" class="btn-float yellow"><i class="fa fa-search"></i></a>
                    <a href="#" class="btn-float blue"><i class="fa fa-cloud-download"> </i></a>
                    <a href="#" class="btn-float green"><i class="fa fa-paperclip"> </i></a>
                    <a href="#" class="btn-float purple"><i class="fa fa-line-chart"> </i></a>
                </div>
            </div>
        </section>
        <section class="model-3">
            <div class="float-btn-group">
                <button class="btn-float btn-triger pink" @click="trigger(1)">
                    <i class="icon-bars"></i>
                </button>
                <div class="btn-list">
                    <a href="#" class="btn-float yellow"><i class="fa fa-search"></i></a>
                    <a href="#" class="btn-float blue"><i class="fa fa-cloud-download"> </i></a>
                    <a href="#" class="btn-float green"><i class="fa fa-paperclip"> </i></a>
                    <a href="#" class="btn-float purple"><i class="fa fa-line-chart"> </i></a>
                </div>
            </div>
        </section>
        <section class="model-6">
            <div class="float-btn-group">
                <button class="btn-float btn-triger pink" @click="trigger(2)">
                    <i class="icon-bars"></i>
                </button>
                <div class="btn-list">
                    <a href="#" class="btn-float yellow"><i class="fa fa-search"></i></a>
                    <a href="#" class="btn-float blue"><i class="fa fa-cloud-download"> </i></a>
                    <a href="#" class="btn-float green"><i class="fa fa-paperclip"> </i></a>
                    <a href="#" class="btn-float purple"><i class="fa fa-line-chart"> </i></a>
                </div>
            </div>
        </section>
    </article>
</template>
<script>
    // import $ from "../assets/js/jquery-2.1.1.min.js"
    // window.jQuery = $;
    // window.$ = $;
    export default {
        name: "Demo2",
        methods: {
            trigger(num) {
                // $(this).closest(".float-btn-group").toggleClass("open")
                // document.querySelector('.float-btn-group').classList.toggle('open');
                document
                    .querySelectorAll(".float-btn-group")[num].classList.toggle("open");
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
    @import "../assets/css/htmleaf-demo.css";
    @import "../assets/css/normalize.css";
    @import "../assets/css/default.css";
    @import "../assets/css/stylesDemo2.css";
    @import "http://cdn.bootcss.com/font-awesome/4.4.0/css/font-awesome.min.css";
</style>