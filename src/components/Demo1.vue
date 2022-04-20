<template>
    <!-- <div class="htmleaf-container"> -->
        <!-- <header class="htmleaf-header">
            <h1>css剪裁GIF背景图片动画特效 <span>Clipping gif to text</span></h1>
            <div class="htmleaf-links">
                <a class="htmleaf-icon icon-htmleaf-home-outline" href="http://www.htmleaf.com/" title="jQuery之家"
                    target="_blank"><span> jQuery之家</span></a>
                <a class="htmleaf-icon icon-htmleaf-arrow-forward-outline"
                    href="http://www.htmleaf.com/css3/css3donghua/202001175892.html" title="返回下载页"
                    target="_blank"><span> 返回下载页</span></a>
            </div>
        </header> -->
        <div class="wrapper">
            <div class="text" data-text="202020">202020</div>
        </div>
    <!-- </div> -->

</template>

<style>
    /* @import "//netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"; */
    /* @import "../assets/css/normalize.css"; */
    /* @import "../assets/css/htmleaf-demo.css"; */

    .wrapper {
        background: #252854;
        width: 100%;
        height: 500px;
        border-radius: 5px;
        position: relative;
    }

    .text {
        flex: 0 0 100%;
        font-size: 14rem;
        font-weight: 900;
        color: #00000000;
        text-align: center;
        font-family: 'Lato', sans-serif;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        border-bottom: 1px solid #d4d7ff;
        border-top: 1px solid #d4d7ff;
        background: url(../assets/img/source.gif);
        background-clip: text;
        -webkit-background-clip: text;
    }

    .text:after {
        content: attr(data-text);
        -webkit-text-stroke: 1.5px #d4d7ff;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -49%);
        background: url(../assets/img/source.gif);
        background-clip: text;
        -webkit-background-clip: text;
        background-size: 43%;
    }
</style>