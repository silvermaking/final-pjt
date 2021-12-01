import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import createPersistedState from "vuex-persistedstate";
// import SERVER from "@/api/server.js"


Vue.use(Vuex)

export default new Vuex.Store({
  // plugins: [createPersistedState()],
  state: {
    movieCards: [],
    movies: [],
    review_list: [],
    recomment_list: [],
    movie_count: 9000000000,
    user_movie: {},
    total: new Array(1000).fill(0),

    content: null,
    like: false,
    rate: null,
    reviw_update: null,

    login: false,
    login_user: null,
    is_admin: false,
    username: null,

    commments: [],
  },
  mutations: {
    IS_ADMIN: function (state, status) {
      state.is_admin - status
    },
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    RECOMMEND_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    CREATE_MOVIE: function (state, movieItem) {
      state.movies.push(movieItem)
    },

  },
  actions: {
    isAdmin: function ({commit}, status) {
      commit('IS_ADMIN', status)
    },
    LoadMovieCards: function ({ commit }) {
      axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/movies/',
        params: {
          // api_key: '3f01e6a52926bb7d09a7f283c6cb86eb',
          // language: 'ko-KR',
        }
      })
        .then(res => {
          console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data)
        })
    },
    createMovie: function ({ commit }, movieItem) {
      commit('CREATE_MOVIE', movieItem)
    },
    RecommendMovieCards: function ({ commit }) {
      axios({
        methods: 'get',
        url: 'http://127.0.0.1:8000/movies/recommend/',
        params: {
          // api_key: '3f01e6a52926bb7d09a7f283c6cb86eb',
          // language: 'ko-KR',
        }
      })
        .then(res => {
          console.log(res)
          commit('RECOMMEND_MOVIE_CARDS', res.data)
        })
    },
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  },
  modules: {
  }
})