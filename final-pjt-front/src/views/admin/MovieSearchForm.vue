<template>
  <div class="container">
    <h1 class="font-do">영화 추가</h1>
    <div class="mb-5 mt-3">
      <label for="search" class="mx-3 font-do">Search: </label>
      <input type="text" id="search" v-model.trim="search" 
        @keypress.enter="searchMovie">
    </div>

    <div class="row" v-if="movies.length">
      <div class="col-3 h-50 w-100 my-3" v-for="(movie,idx) in movies" :key="idx">
        <div class="card bg-dark">
          <img class="card-img-top" :src="movie.poster_path" :alt="movie.title">
          <div class="card-body">
            <h5 class="card-text text-white font-poor"> {{movie.title}} </h5>
            <button @click="addMovie(movie)" class="btn">이 영화 추가</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const SEARCH_URL = process.env.VUE_APP_SEARCH_URL
const API_KEY = process.env.VUE_APP_API_KEY
import axios from 'axios'
export default {
  name: 'MovieSearchForm',
  data: function () {
    return {
      search: null,
      movies: [],
      img_url: "http://image.tmdb.org/t/p/w185",
    }
  },
  methods: {
    searchMovie: function () {
      if (this.search) {
        this.movies =[]
        axios({
          method: 'get',
          url: `${SEARCH_URL}=${API_KEY}&language=ko-KR&query=${this.search}&page=1&include_adult=false`,
        })
          .then(res => {
            for (const movie of res.data.results) {
              // console.log(movie)
              const temp = {
                movie_no: movie.id,
                title: movie.title,
                release_date: movie.release_date,
                poster_path: this.img_url + movie.poster_path,
                overview: movie.overview,
                genres: movie.genre_ids,
              }
              if (movie.poster_path === null) {
                temp.poster_path = ''
              }
              // console.log(temp)
              this.movies.push(temp)
            }
          })
          .catch(err => {
            console.log(err)
          })
        this.search = null
      }
    },
    addMovie: function (movie) {
      const movieItem = {
        movieInfo: {
        movie_no: movie.movie_no,
        title: movie.title,
        release_date: movie.release_date,
        poster_path: movie.poster_path,
        adult: false,
        overview: movie.overview,
        status: false,
        admin_reg: true,
      }, genreInfo: {
        genres: movie.genres
      }}
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/movies/add/',
        data: movieItem
      })
        .then(res => {
          // console.log(r동으로 vuex에서 관리하는 영화목록에 추가
          this.$store.state.movie_list.push(res.data)
          this.$router.push({ name: 'ManageMovie' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  mounted() {
      window.scrollTo(0,0)
  }
  
}
</script>

<style scoped>
.card-img-top {
  width: 100%;
  height: 30vw;
  object-fit: cover;
}
</style>