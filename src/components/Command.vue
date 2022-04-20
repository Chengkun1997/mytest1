<template>
  <div id="command">
    <div v-html="message"><p>使用 v-html 指令用于输出 html 代码</p></div>
    <p v-if="seen">能看见我了</p>
    <template v-if="ok"><h1>看我看我</h1></template>
    <div v-if="(ra = Math.random() > 0.5)">{{ ra }}Sorry</div>
    <div v-else>Not sorry</div>
    <div v-show="Math.random() > 0.5">看不见时我也在</div>
    <ol>
      <!-- <li v-for="(item, index) in sites"> {{ item.name }}, {{ index }}</li> -->
    </ol>
    <span v-bind:class="{ className: isActive }" style="display: block"
      >ddd</span
    >
    <button v-on:click="onClick">按钮</button>
    <!-- <button @click="onClick"></button> -->
    <p>v-model 指令在表单控件元素上创建双向数据绑定（初始值）</p>
    <input v-model="inputSomething" />
    <input v-model.lazy="inputSomething" />
    <p>数据双向绑定：{{ inputSomething }}</p>
    <!-- <input v-model.number="age" type=”number”>自动转为 Number 类型 -->
    <!-- <input v-model.trim="msg" >自动过滤用户输入的首尾空格 -->
    <p>原始字符串: "{{ message }}"</p>
    <p>计算后反转字符串: "{{ reversedMessage }}"</p>
    <p style="font-size: 25px">计数器：{{ counter }}</p>
    <button @click="counter++">点击计数</button>
  </div>
</template>

<script>
export default {
  // el: "#command",
  name: "Command",
  data() {
    return {
      message: "<h1>Vue语法介绍</h1>",
      seen: true,
      ok: 1,
      sites: [{ name: "Aa" }, { name: "Bb" }, { name: "Cc" }],
      isActive: true,
      inputSomething: "双向数据绑定（初始值）",
      counter: 1,
    };
  },
  methods: {
    // onClick:function(){
    onClick() {
      console.log(this.message, this.seen, this.sites, this.isActive);
    },
  },
  computed: {
    // reversedMessage() {
    reversedMessage: function () {
      return this.message.split('').reverse().join('');//`this` 指向 vm 实例
    },
  },
  mounted() {
    this.$watch("counter", function (newVal, oldVal) {
      alert("计数器值的变化 :" + oldVal + " 变为 " + newVal + "!");
    });
  },
};
</script>

<style>
</style>