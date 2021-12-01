<template>
  <div>
    <input 
      type="text"
      v-model.trim="movieTitle"
      @keyup.enter="createMovie"
    >
    <button @click="createMovie">Add</button>
  </div>
</template>

<script>
export default {
  name: 'MovieListForm',
  data: function () {
    return {
      movieTitle: null,
    }
  },
  methods: {
    createMovie: function () {
      const movieItem = {
        title: this.movieTitle,
        date: new Date().getTime(),
      }
      if (movieItem.title) {
        this.$store.dispatch('createMovie', movieItem)
      }
      this.movieTitle = null
    }
  }
}
</script>

<style>

</style>