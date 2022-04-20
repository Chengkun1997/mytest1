<template>
    <div>
        <section>
            <h2>从本地上传原图片到网页</h2>
            <!-- // 这种可以打开相机或文件，"jpg,png,gif"这种打开只能上传特定文件且没有相机," -->
            <input type="file" accept="image/*" @change="changeImage()" ref="avatarInput" style="display:none">
            <!-- 隐藏原生上传控件style="display:none，使用自己上传的图标，并添加element-ui的图片预览功能 -->
            <!-- 使用自己上传的图标 -->
            <img class="upload_btn" @click="upLoad" src="../assets/img/Icon/out.png" />
            <div class="pic_list_box">
                <div class="pic_list" v-show="imgDatas.length">
                    <div v-for="(src,index) in imgDatas" :key="index">
                        <!-- 利用element-ui的图片预览插件 -->
                        <el-image style="width: 100px; height: 100px" :src="src" :preview-src-list="imgDatas">
                        </el-image>
                    </div>
                </div>
            </div>
        </section>
        <section>
            <h2>可以blob</h2>
            <el-upload action="" :on-change="handleelchange" :auto-upload="false" list-type="picture-card">
                <i class="el-icon-plus"></i>
            </el-upload>
        </section>
        <section>
            <h2>从网页下载原图片到本地</h2>
            <img id="images_http"
                src="http://e.hiphotos.baidu.com/image/pic/item/1c950a7b02087bf49661186dffd3572c10dfcfa1.jpg" alt=""
                width="300" />
            <img id="images_file" src="../assets/logo.png" alt="" />
            <button @click="download('images_http','pic_http')">点击下载http图片</button>
            <button @click="download('images_file','pic_file')">点击下载file图片</button>
        </section>
        <section>
            <h2>在本地预测，将结果图片自动上传到网页</h2>
            <button @click="getData">getData测试python连接数据库</button>
        </section>
    </div>
</template>

<script>
    import 'element-ui/lib/theme-chalk/index.css';
    // import logo from "../assets/logo.png";
    const axios = require('axios');
    export default {
        name: "Demo5",
        data() {
            return {
                imgDatas: [],
            }
        },
        methods: {
            getData() {
                axios.get("http://127.0.0.1:5000/getAll").then(res => {
                    console.log(res)
                })
            },
            postData(inputData){
                console.log("inputData:", inputData)
                // let paramsData={
                //     "inputData": 'blob:http://localhost:8080/40cc3a38-9d88-4eb8-bc13-22c8c248a06d'
                // }
                let paramsData={
                    "inputData": inputData
                }
                // 调用python 服务接口时，带上参数paramsData
                axios.post("http://127.0.0.1:5590/picApp", paramsData).then(res => {
                    
                    console.log("paramsData:", paramsData)
                    console.log("paramsData.inputData:", paramsData.inputData)
                    console.log("res:", res)
                })
            },
            handleelchange(file, fileList) {
                console.log("file：", file)
                console.log("file.url：", file.url)
                console.log("fileList：", fileList)

                let formdata = new FormData()
                fileList.map(item => { //fileList本来就是数组，就不用转为真数组了
                    formdata.append("file", item.raw) //将每一个文件图片都加进formdata
                })
                console.log("formdata:", formdata)
                let data=file.url
                this.postData(data)
                //    axios.post("接口地址", formdata).then(res => { console.log(res) })
                // axios.post("http://127.0.0.1:5590/picApp", formdata).then(res => {
                //     console.log("res:", res)
                // })
            },
            
//#region 
            upLoad() {
                // 触发上传图片按钮，进而触发changeImage（）
                this.$refs.avatarInput.dispatchEvent(new MouseEvent("click"));
            },
            changeImage() {
                // 上传图片事件
                var files = this.$refs.avatarInput.files;
                console.log("files:", files)
                console.log("files[0]:", files[0])
                console.log("files[1]:", files[1])
                console.log("files.length:", files.length)
                console.log("imgDatas:", this.imgDatas)
                var that = this;

                function readAndPreview(file) {
                    //Make sure `file.name` matches our extensions criteria
                    if (/\.(jpe?g|png|gif)$/i.test(file.name)) {
                        var reader = new FileReader();
                        reader.onload = function (e) {
                            // 防止重复上传
                            if (that.imgDatas.indexOf(e.target.result) === -1) {
                                that.imgDatas.push(e.target.result);
                            }
                        };
                        reader.readAsDataURL(file);
                    }
                }
                readAndPreview(files[0])
                if (files.length === 0) {
                    return;
                }

                // 文件上传服务器
                this.setUploadFile(files[0])

            },
            setUploadFile(file) {
                this.formData = new FormData()
                console.log("file",file)
                this.formData.append('files', file, file.name) // 添加到请求体
                console.log("formData",this.formData)
                axios.post('http://127.0.0.1:5459/picApp2', this.formData).then(res => {
                    console.log(res);
                })
            //     // this.$http
            //     //     .post('/api/dxbase/upload?resType=EVENT', this.formData)
            //     //     .then(res => {
            //     //         console.log(res);
            //     //     })
            },
//#endregion


            download(link, picName) {
                console.log(111);
                const image = new Image();
                // 解决跨域 canvas 污染问题
                image.setAttribute("crossOrigin", "anonymous");
                image.onload = function () {
                    const canvas = document.createElement("canvas");
                    canvas.width = image.width;
                    canvas.height = image.height;
                    const context = canvas.getContext("2d");
                    context.drawImage(image, 0, 0, image.width, image.height);
                    //得到图片的base64编码数据
                    const url = canvas.toDataURL("image/png");
                    // 生成一个 a 标签
                    const a = document.createElement("a");
                    // 创建一个点击事件
                    const event = new MouseEvent("click");
                    // 将 a 的 download 属性设置为我们想要下载的图片的名称，若 name 不存在则使用'图片'作为默认名称
                    a.download = picName || "图片";
                    // 将生成的 URL 设置为 a.href 属性
                    a.href = url;
                    // 触发 a 的点击事件
                    a.dispatchEvent(event);
                    // return a;
                };
                image.src = document.getElementById(link).src;
                // image.src = document.getElementById("images").src;
                // img.src = link + '?v=' + Date.now()
            },

        }
    };
</script>

<style scoped>
    .pic_list_box {
        display: flex;
    }

    .upload_btn {
        width: 100px;
        height: 100px;
        padding-left: 15px;
    }

    .pic_list {
        display: flex;
    }
</style>