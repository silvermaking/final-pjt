<template>
  <div class="container">
    <div class="row">
    <hr>
    </div>

    <form v-on:submit.prevent="updateComment">
      <div class="row">
      <div class="col-2 d-flex align-items-center" id="updateDiv">
        <label for="content">댓글 수정: </label>
      </div>
      <div class="col-6 d-flex align-items-center">
        <input type="text" class="form-control" id="content" v-model="content">
        </div>
      <div class="col-4 d-flex align-items-center">
      <button type="submit" @click="updateComment(board)" class="btn">수정완료</button>
      </div>
      </div>
    </form>
    
  </div>

</template>

<script>
  import axios from 'axios'

  export default {
    name: 'CreateComment',
    data: function () {
      return {
        content: null,
        comments: null,
      }
    },
    props: {
      updateCommentItem: [],
      board: [],
    },
    methods: {
      setToken: function () {
        const token = localStorage.getItem('jwt')
        const config = {
          headers: {
            Authorization: `JWT ${token}`
          }
        }
        return config
      },
      updateComment: function () {
        const updateItem = {
          ...this.updateCommentItem,
        }
        axios({
          method: 'put',
          url: `http://127.0.0.1:8000/community/${this.board.id}/comment/${this.updateCommentItem.id}/`,
          data: updateItem,
          headers: this.setToken()
        })
          .then(res => {
            console.log(res)
          })
          .catch(err => {
            console.log(err)
          })
      },
    },
    created: function () {
      this.content = this.updateCommentItem.content
      this.comments = this.$store.state.comments
    },
  }
</script>

<style scoped>

</style>