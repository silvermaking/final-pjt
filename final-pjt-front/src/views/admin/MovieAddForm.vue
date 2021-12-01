<template>
  <div class="font-poor">
    <b-container>
      <b-row class="d-flex justify-content-center">
        <h1 class="my-5 font-do">영화 추가</h1>
        
      </b-row>



      <b-row class="my-1">
        <b-col sm="2" offset="2">
          <label for="title">Title: </label>
        </b-col>
        <b-col sm="6">
          <b-form-input id="title" v-model.trim="title"></b-form-input>
        </b-col>
      </b-row>

      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="release_date">Release Date: </label>
        </b-col>
        <b-col sm="6">
          <input type="date" id="release_date" v-model="release_date">
        </b-col>
      </b-row>


      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="adult">Adult: </label>
        </b-col>
        <b-col sm="6">
          <input type="checkbox" id="adult" checked="true" v-model="adult">
          <label for="adult">성인영화</label>
        </b-col>
      </b-row>


      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="status">Status: </label>
        </b-col>
        <b-col sm="6">
          <input type="checkbox" id="status" checked="true" v-model="status">
          <label for="status">상영중</label>
        </b-col>
      </b-row>


      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="overview">Overview: </label>
        </b-col>
        <b-col sm="6">
          <b-form-input type="text" id="overview" v-model.trim="overview"></b-form-input>
        </b-col>
      </b-row>

      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label for="poster_path">Poster path: </label>
        </b-col>
        <b-col sm="6">
          <b-form-input type="text" id="poster_path" v-model.trim="poster_path" placeholder="이미지 없으면 # 입력"></b-form-input>
        </b-col>
      </b-row>
      <b-row class="my-3">
        <b-col sm="2" offset="2">
          <label>Genres: </label>
        </b-col>
      </b-row>

      <b-col sm="8" offset="3">
        <b-form-group>
          <b-form-checkbox-group id="genre" v-model="checked_genres" name="genre">
            <b-form-checkbox v-for="(genre,idx) in genres" :key="idx" :value="genre.id">{{ genre.name }}</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
      </b-col>

      <br>
      <b-button variant="secondary" @click="back" class="my-5 mx-3 font-jua">취소</b-button>
      <b-button  @click="addMovie" class="my-5 btn">추가</b-button>
    </b-container>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'MovieAddForm',
  data: function () {
    return {
      genres: '',
      title: null,
      release_date: null,
      adult: false,
      status: false,
      overview: null,
      poster_path: null,
      checked_genres: [],
    }
  },
  created: function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/movies/genre/',
    })
      .then(res => {
        // console.log(res.data)
        this.genres = res.data
      })
      .catch(err => {
        console.log(err)
      })
  },
  methods: {
    back: function () {
      this.$router.push({ name: 'ManageMovie' })
    },
    addMovie: function () {
      const temp_number = this.$store.state.movie_count
      // poster_path가 공란이면
      const movieItem = {
        movieInfo: {
        movie_no: temp_number,
        title: this.title,
        release_date: this.release_date,
        poster_path: this.poster_path,
        adult: this.adult,
        overview: this.overview,
        status: this.status,
        admin_reg: true,
      }, genreInfo: {
        genres: this.checked_genres
      }}
      // console.log(movieItem)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/movies/add/`,
        data: movieItem
      })
        .then(res => {
          // console.log(res)
          this.$store.state.movie_count++
          // 영화를 만들면 자동으로 vuex에서 관리하는 영화목록에 추가
          this.$store.state.movie_list.push(res.data)
          this.$router.push({ name: 'ManageMovie' })
        
        })
        .catch((err) => {
          alert("모든 항목을 채워주세요.")
          console.log(err)
        })
    },
  },
  mounted() {
      window.scrollTo(0,0)
  }
}
</script>

<style>
</style>