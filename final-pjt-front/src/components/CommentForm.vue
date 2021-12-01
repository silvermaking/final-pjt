<template>
  <div>
    <input 
      type="text"
      v-model.trim="content"
      @keyup.enter="createComment"
    >
    <button @click="createComment">등록</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentForm',
  data: function () {
    return {
      content: null,
    }
  },
  props: {
    board: [],
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createComment: function () {
      const commentItem = {
        content: this.content
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/${this.board.id}/comment_create/`,
        data: commentItem,
        headers: this.setToken()
      })
        .then(res => {
          this.$store.state.comments.unshift(res.data)
          this.content = null
        })
        .catch(err => {
          console.log(err)
        })
    },
    created: function () {
      console.log(this.board)
    }
  }
}
</script>

<style>

</style>