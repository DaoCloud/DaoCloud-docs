import { type App } from 'vue';
import {
  createRouter, createWebHistory, type Router, type RouteRecordRaw, type RouterHistory,
} from 'vue-router';
import HomeView from '../views/HomeView.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },
];

let router: Router | null = null;
let history: RouterHistory | null = null;

export default (app: App, basePath = '') => {
  history = createWebHistory(basePath || process.env.VUE_APP_ROUTER_BASE_PATH);
  router = createRouter({
    history,
    routes,
  });
  app.use(router);
};

export const destroyRouter = () => {
  if (history && history.destroy) {
    history.destroy();
  }
  router = null;
};
