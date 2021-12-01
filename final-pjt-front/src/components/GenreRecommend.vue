<template>
  <v-container fluid>
    <v-layout row  wrap class="d-flex justify-content-between align-items-center">

      <v-container fluid class="d-flex" style="overflow:auto">
        <v-flex v-for="movie in this.favoriteGenreMovieList" :key="movie.id" class="justify-content-center" style="min-width: 200px;">
          <MovieCard class="mx-3" :movie="movie" />
        </v-flex>
      </v-container>
    </v-layout>

  </v-container>
</template>

<script>
import axios from "axios";
import jwtDecode from "jwt-decode";
import MovieCard from "@/components/MovieCard.vue";
export default {
	components: {
    MovieCard
  },
  data() {
    return {
      favoriteGenreMovieList: [],
    };
  },
 
  methods: {
    getGenreMovieList() {
      const token = sessionStorage.getItem("jwt");
      const SERVER_URL = "http://127.0.0.1:8000";
      const user_id = jwtDecode(token).user_id;
      const options = {
        headers: {
          Authorization: "JWT " + token
        }
      };
      axios
        .get(`${SERVER_URL}/api/v1/${user_id}/like_genre/`, options)
        .then(res => {
          console.log(res)
          this.favoriteGenreMovieList = res.data
        });
    }
  },
  watch: {
  },
  created() {
    this.getGenreMovieList()
  }
};
</script>

<style>
</style>