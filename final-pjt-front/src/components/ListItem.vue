<template>
  <div>
    <p>{{ movie.title }}</p>
  </div>
</template>

<script>
export default {
  name: 'ListItem',
  props: {
    movie: {
      type: Object,
    }
  },
  methods: {

  },
}
</script>

<style>

</style>