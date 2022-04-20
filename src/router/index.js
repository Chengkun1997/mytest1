import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import( /* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/helloWorld',
    name: 'HelloWorld',
    component: () => import('../components/HelloWorld.vue')
  },
  {
    path: '/demo1',
    name: 'Demo1',
    component: () => import('../components/Demo1.vue')
  },
  {
    path: '/demo2',
    name: 'Demo2',
    component: () => import('../components/Demo2.vue')
  },
  {
    path: '/demo3',
    name: 'Demo3',
    component: () => import('../components/Demo3.vue'),
  },
  {
    path: '/cssTest',
    name: 'CssTest',
    component: () => import('../components/CssTest.vue'),
  },
  {
    path: '/cssAnimate',
    name: 'CssAnimate',
    component: () => import('../components/CssAnimate.vue'),
  },
  {
    path: '/demo5',
    name: 'Demo5',
    component: () => import('../components/Demo5.vue'),
  },
  {
    path: '/demo2sample',
    name: 'Demo2sample',
    component: () => import('../components/Demo2sample.vue'),
  },
  {
    path: '/WebAIdemo',
    name: 'WebAIdemo',
    component: () => import('../components/WebAIdemo.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router