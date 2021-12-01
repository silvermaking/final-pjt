<template>
  <div>
    <h1>Recommend</h1>
    <div class="container">
      <div class="row">
        <movie-card
          class='card col-lg-4 col-sm-4 col-xs-6 mb-3'
          v-for="movieCard in movieCards"
          :key="movieCard.id"
          :movieCard="movieCard"
        >
        </movie-card>
      </div>
      <!-- <button @click="pickRandomMovie">Pick</button>
      <br>
      <img 
        :src="`https://127.0.0.1.8000/movies/recommend`" 
        alt="Pick a MOVIE"
      > -->


    </div>
  </div>
</template>
<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from "vuex"

export default {
  name: 'Random',
  components: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('RecommendMovieCards')
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



// import _ from 'lodash'
// import { mapState } from "vuex"

// export default {
//   name: 'Random',
//   data: function () {
//     return {
//       randomMovie : "",
//     }
//   },
//   methods: {
//     pickRandomMovie: function () {
//       const movies = this.$store.state.movieCards
//       this.randomMovie = (_.sample(movies)).poster_path
//     }
//   },
//   computed: {
//     ...mapState(['movieCards']),
//   }
  
<<<<<<< HEAD
// }
=======
// }
>>>>>>> aeb8f9c84b9f054529e347699abcf824faf3d5f1
