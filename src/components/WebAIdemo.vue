<template>
    <div>
        Image:
        <!-- <input type="file" accept="image/*" id="inputFile" disabled='false'> -->
        <input type="file" accept="image/*" id="inputFile">
        <p>ssss</p>
        <!-- <img src="" alt="" id="imgDom" style="display: none"> -->
        <img src="" alt="" id="imgDom">
        <canvas id='canvasDom'></canvas>
    </div>
</template>
<script>
//import WebAI
// import WebAI from 'webai-js'
// const WebAI = require('webai-js')
// import 'https://cdn.jsdelivr.net/npm/webai-js/dist/webai.min.js'
//set wasm path of the onnxruntime-web
// WebAI.ort.env.wasm.wasmPaths = "https://cdn.jsdelivr.net/npm/webai-js/dist/"
export default {
    name: "WebAIdemo",
    // mounted(){
    //     const WebAI = require('webai-js/src/webai.js')
    //     // Get HTML elements
    //     const imgDom = document.getElementById('imgDom')
    //     const canvasDom = document.getElementById('canvasDom')
    //     const inputFile = document.getElementById('inputFile')

    //     // Face detection model files
    //     const modelURL = 'https://agentmaker.github.io/WebAI.js/pages/pretrained_models/det/blazeface_1000e/model.onnx'
    //     const modelConfig = 'https://agentmaker.github.io/WebAI.js/pages/pretrained_models/det/blazeface_1000e/configs.json'

    //     // Detection threshold
    //     // const drawThreshold = 0.5;

    //     // Load the model
    //     window.onload = async function (e) {
    //         window.model = await WebAI.Det.create(modelURL, modelConfig)
    //     }

    //     // Set the input image
    //     this.inputFile.onchange = function (e) {
    //         if (e.target.files[0]) {
    //             imgDom.src = URL.createObjectURL(e.target.files[0])
    //         }
    //     }

    //     // Model infer and show the result image
    //     this.imgDom.onload = async function (e) {
    //         let imgRGBA = cv.imread(imgDom)
    //         let bboxes = await model.infer(imgRGBA)
    //         let imgShow = await WebAI.drawBBoxes(imgRGBA, bboxes)
    //         cv.imshow(canvasDom, imgShow)
    //         imgRGBA.delete()
    //         imgShow.delete()
    //     }
    // }
}
</script>