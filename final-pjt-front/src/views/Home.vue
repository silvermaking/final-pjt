<template>
  <div class="home">
    <div class="area" style="background-color: #000000; color: #ffffff;">
      <div class="logo">
        <!-- <h1 style="color: blue; font-size: 100px;" alt>SSAFLIX</h1> -->
      </div>
      <a class="title_area">
        <!-- <strong class="title">무비는 싸플릭스</strong> -->
      </a>
      <div class='row'>
          <movie-card
            class='card col-lg-4 col-sm-4 col-xs-6 mb-3'
            v-for="movieCard in movieCards"
            :key="movieCard.id"
            :movieCard="movieCard"
          >
          </movie-card>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from "vuex"

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards']),
  }
}
</script>

<style>
.area{
  color: black;
}
</style>