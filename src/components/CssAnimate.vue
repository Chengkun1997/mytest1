<template>
    <div>
        <el-button type="primary" plain @click="isOpen=!isOpen">开关动画</el-button>
        <img src="../assets/img/礼物盒子1.png" alt="礼物盒子..." id="giftBoxClose" />
        <el-button type="primary" plain @click="isShake">抖动动画</el-button>
    </div>
</template>
<script>
    export default {
        name: "CssAnimate",
        data() {
            return {
                isOpen: true,
                giftBoxClose: "",
            }
        },
        methods: {
            isShake(){
this.giftBoxClose.classList.add("shakeHi");
setTimeout(() => {
    this.giftBoxClose.classList.remove("shakeHi");
}, 3000);
            },
        },
        mounted() {
            this.giftBoxClose = document.getElementById("giftBoxClose");
            this.giftBoxClose.classList.add("anicssBounce");
        },
        watch: {
            isOpen(newV, oldV) {
                console.log("新值" + newV + "， 旧值：" + oldV)
                if (this.isOpen) {
                    this.giftBoxClose.classList.add("anicssBounce");
                } else {
                    this.giftBoxClose.classList.remove("anicssBounce");
                }
            }

        },
    }
</script>
<style scoped>
    @import "../assets/css/animate.min.css";

    #giftBoxClose {
        /* position: absolute;
  left: calc(43.5%);
  bottom: calc(13%);
  height: 236px;
  width: 205px;
  z-index: 10; */
  margin:80px; /* 外边距 */
  padding: 80px;   /* 内边距 */
        /* animation: rotate 0.5s linear infinite; */
        /* animation: shake 1000ms ease-in-out; */
        /* animation: pulse; */
        /* animation-duration: 3s; */
        /* animation: pulse 2.5s infinite; */
    }

    .anicssBounce {
        animation: pulse 2.5s infinite;
    }

    .shakeHi {
        animation: shakeHi 1000ms ease-in-out;
    }

    /* 水平抖动，核心代码 */
    @keyframes shakeHi {

        10%,
        90% {
            transform: translate3d(-1px, 0, 0);
        }

        20%,
        80% {
            transform: translate3d(+2px, 0, 0);
        }

        30%,
        70% {
            transform: translate3d(-4px, 0, 0);
        }

        40%,
        60% {
            transform: translate3d(+4px, 0, 0);
        }

        50% {
            transform: translate3d(-4px, 0, 0);
        }
    }
</style>