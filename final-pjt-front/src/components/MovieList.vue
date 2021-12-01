<template>
  <div>
    <v-card class="mx-auto" max-width="800">
      <v-toolbar color="grey">
        <v-toolbar-title>Movie List</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-toolbar>

      <v-container fluid v-if="isLoggedIn">
        <v-row>
          <v-col v-for="movie in movies" :key="movie.id" :cols="6" sm="3">
            <MovieCard :movie="movie" />
          </v-col>
        </v-row>
      </v-container>
      <v-container v-else>
        <h5 class="my-3">영화 목록을 보려면 로그인을 먼저 해주세요!</h5>
        <v-btn color="blue-grey" class="ma-2 white--text" href="/login">
          Log in
          <v-icon right dark>mdi-account-check</v-icon>
        </v-btn>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import MovieCard from "@/components/MovieCard.vue";
import { mapGetters } from "vuex";
export default {
  name: "MovieList",
  components: {
    MovieCard
  },
  props: {
    movies: {
      type: Array
    },
  },
  data() {
    return {
      col_flex: 3
    };
  },
  computed: {
    ...mapGetters(["isLoggedIn"])
  }
};
</script>

<style>
</style>