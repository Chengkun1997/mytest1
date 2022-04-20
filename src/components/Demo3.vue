<template>
    <div class="htmleaf-container">
        <header class="htmleaf-header">
            <h1>基于canvas的动态马赛克文字特效</h1>
            <div class="htmleaf-links">
                <a class="htmleaf-icon icon-htmleaf-home-outline" href="http://www.htmleaf.com/" title="jQuery之家"
                    target="_blank"><span> jQuery之家</span></a>
                <a class="htmleaf-icon icon-htmleaf-arrow-forward-outline"
                    href="http://www.htmleaf.com/html5/html5-canvas/202001065882.html" title="返回下载页"
                    target="_blank"><span> 返回下载页</span></a>
            </div>
        </header>
        <button @click="show">来吧展示</button>
        <div class="htmleaf-content">
            <input type="text" id="input" placeholder="请输入内容" value="" title="type and press enter" />
        </div>
        <!-- <scriptLink></scriptLink> -->
        <!-- <remote-js src="'https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js'"></remote-js> -->
    </div>
</template>
<script>
    // import "https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js";
    // import "../assets/js/underscore-min.js"
    // import "../assets/js/script.js"
    // import "../../public/js/underscore-min.js"
    // import "../../public/js/script.js"  

    export default {
        name:"Demo3",
        components: {
            // 'scriptLink': {
            //     render(createElement) {
            //         return createElement(
            //             'script', {
            //                 attrs: {
            //                     type: 'text/javascript',
            //                     src: '../../public/js/script.js',
            //                 },
            //             },
            //         )
            //     }
            // },
            // 'remote-js': {
            //     render(createElement) {
            //         return createElement('script', {
            //             attrs: {
            //                 type: 'text/javascript',
            //                 src: this.src
            //             }
            //         });
            //     },
            //     props: {
            //         src: {
            //             type: String,
            //             required: true
            //         }
            //     }
            // }

        },
        data() {
            return {
                oScript: "",
                oScriptTemp: "",
            }
        },
        methods: {
            show() {
                this.oScriptTemp = document.createElement('script');
                console.log("this.oScriptTemp", this.oScriptTemp)
                this.oScriptTemp.type = 'text/javascript';
                // oScript.src = 'https://unpkg.com/element-ui@2.3.7/lib/index.js';
                this.oScriptTemp.src = "js/scriptDemo3.js";
                document.body.appendChild(this.oScriptTemp);
                this.isShow = true;
            },
        },
        mounted() {
            this.oScript = document.createElement('script');
            this.oScript.type = 'text/javascript';
            this.oScript.src = 'https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js';
            // oScript.src = "js/script.js";
            document.body.appendChild(this.oScript);
        },
        // beforeRouteEnter(to, from, next) {
        //     console.log(to, from, next)
        //     // next(vm => {
        //     //     // 通过 `vm` 访问组件实例
        //     // })
        // },
        // beforeRouteUpdadte() {},
        beforeRouteLeave(to, from, next) {
            console.log(to, from, next)
            if (this.oScriptTemp) {
                // document.body.removeChild(this.oScriptTemp) //不起作用
                // document.body.removeChild(this.oScript)
                location.reload()
            }
            //  this.$router.push(from);
             next()
            // console.log(to, from, next)
            // setTimeout(() => {
            //     next()
            // }, 300);
            // if (this.oScriptTemp) {
            //     document.body.removeChild(this.oScriptTemp)
            //     document.body.removeChild(this.oScript)
            //     const answer = window.confirm('Do you really want to leave? you have unsaved changes!')
            //     if (answer) {
            //         // location.reload()
            //         this.$router.go(to)
            //         next()
            //     } else {
            //         next(false)
            //     }
            // } else {
            //     next()
            // }
            // const answer = window.confirm('Do you really want to leave? you have unsaved changes!')
            // if (answer) {
            //     next()
            // } else {
            //     next(false)
            // }
        },
    }
</script>

<style>
    @import "../assets/css/normalize.css";
    @import "../assets/css/htmleaf-demo.css";

    #input {
        position: absolute;
        bottom: 10px;
        left: 50%;
        width: 8em;
        max-width: 60%;
        background: none;
        border: none;
        outline: none;
        border-bottom: 2px solid #fff;
        /*输入框下边框 */
        color: #fff;
        font-size: 3em;
        text-align: center;
        z-index: 999;
        opacity: .25;
        -webkit-transform: translateX(-50%);
        transform: translateX(-50%);
        transition: opacity .3s;
    }

    #input:hover,
    #input:focus {
        opacity: 1;
    }

    /* body {
        position: fixed;
        top: 0;
        left: 0;
        width: 50%;
        height: 50%;
        margin: 0;
        padding: 0;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    } */
</style>