import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import Regist from "../components/Regist";
import Index from "../components/Index";
import Add_emp from "../components/Add_emp";
import Update_emp from "../components/Update_emp";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component:Login,
    },
    {
      path: '/Login',
      name: 'Login',
      component:Login,
    },
    {
      path: '/Regist',
      name: 'Regist',
      component:Regist,
    },
    {
      path: '/Index',
      name: 'Index',
      component:Index
    },
    {
      path: '/Add_emp',
      name: 'Add_emp',
      component:Add_emp
    },
    {
      path: '/Update_emp/:id/',
      name: 'Updata_emp',
      component:Update_emp
    },
  ]
})
