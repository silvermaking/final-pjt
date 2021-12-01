<template>
  <div>

    <div class="container">
      <div class="row">
        <h1 class="font-do">영화 리스트</h1>
      </div>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        align="center"
        aria-controls="movieTable"  
      ></b-pagination>
      <div class="row">


      <b-table name="movieTable"
        striped hover :items="movies" :fields="fields" head-variant="dark"
        table-variant="light" :current-page="currentPage" :per-page="perPage" :fixed="true"
        stacked="md" sort-icon
        >

        <template #cell(index)="data">
          {{ data.index + 1 }}
        </template>     


        <template #cell(name)="row">
          {{ row.value.first }} {{ row.value.last }}
        </template>

        <template #cell(actions)="data">
          <b-button @click="updateMovie(data.item)" class="mr-1 btn btn-warning font-jua">
            수정
          </b-button>
          <b-button @click="deleteMovie(data.item)" class="btn btn-secondary font-jua">
            삭제
          </b-button>
        </template>
      
      </b-table>
      </div>
    </div>


  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name: 'AdminMovieList',
  data: function () {
    return {
      perPage: 10,
      currentPage: 1,
      fields: [
        'index',
        { key: 'movie_no', label: '코드' },
        { key: 'title', label: '제목', sortable: true, sortDirection: 'desc' },
        { key: 'release_date', label: '개봉일', sortable: true, sortDirection: 'desc' },
        { key: 'vote_count', label: '추천', sortable: true, sortDirection: 'desc' },
        { key: 'rate', label: '총평점', sortable: true, sortDirection: 'desc' },
        { key: 'actions', label: '관리'}
      ],
    }
  },
  methods: {
    updateMovie: function (movie) {
      this.$router.push( { name: 'MovieUpdateForm', params: {'movie': movie}})
    },
    deleteMovie: function (movie) {
      if (confirm("이 영화를 삭제하겠습니까?"))
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/${movie.id}/movie/`
      })  
        .then(res => {
          const idx = this.movie_list.findIndex((movie) => {
            return movie.id === res.data.id
          })
          this.movie_list[idx].movie_no = 0
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  computed: {
    ...mapState([
      'movie_list',
    ]),
    movies: function () {
      return this.movie_list.filter( (movie) => {
        if (movie.movie_no) {
          return movie
        }
      })
    },
    rows: function () {
      return this.movies.length
    }
  }
}
</script>

<style>
</style>