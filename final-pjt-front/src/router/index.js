import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Random from '@/views/Random.vue'
import MovieList from '@/views/movies/MovieList.vue'
import Board from '@/views/community/Board'
import BoardDetail from '@/views/community/BoardDetail'
import CreateBoard from '@/views/community/CreateBoard'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieAddForm from '@/views/admin/MovieAddForm'
import MovieSearchForm from '@/views/admin/MovieSearchForm'
import MovieUpdateForm from '@/views/admin/MovieUpdateForm'
import ManageMovie from '@/views/admin/ManageMovie'
import AdminManagement from '@/views/admin/AdminManagement'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/random',
    name: 'Random',
    component: Random,
  },
  {
    path: '/movies/movie-list',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/managemovie',
    name: 'ManageMovie',
    component: ManageMovie,
  },
  {
    path: '/community/board',
    name: 'Board',
    component: Board,
  },
  {
    path: `/BoardDetail`,
    name: 'BoardDetail',
    component: BoardDetail,
  },
  {
    path: '/community/createboard',
    name: 'CreateBoard',
    component: CreateBoard,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movieaddform',
    name: 'MovieAddForm',
    component: MovieAddForm,
  },
  {
    path: '/moviesearchform',
    name: 'MovieSearchForm',
    component: MovieSearchForm,
  },
  {
    path: '/movieupdateform',
    name: 'MovieUpdateForm',
    component: MovieUpdateForm,
  },
  {
    path: '/management',
    name: 'AdminManagement',
    component: AdminManagement,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
