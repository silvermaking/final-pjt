<template>
  <div>
    <h1>Movie List</h1>
    <br>
    <list-form></list-form>
    <list></list>
  </div>
</template>

<script>

import ListForm from '@/components/ListForm';

export default {
  name: 'MovieList',
  components: {
    ListForm,
  }
}
</script>

<style>

</style>