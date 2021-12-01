<template>
  <div>
    <div v-if="updateTrigger === comment.id">
      <CreateComment :updateCommentItem="updateCommentItem" :board="board" @trigger="changeTrigger" />
    </div>
    <ul>
      <li v-for="(comment, idx) in comments" :key="idx" class="media mt-3">
        <button @click="updateBoard(comment)" class="btn">댓글수정</button>
        <button @click="deleteComment(comment)" class="btn">댓글삭제</button>
      </li>
    </ul>
  </div>
</template>

<script>
import CreateComment from '@/components/CreateComment'
import axios from 'axios'
import { mapState } from 'vuex'
export default {
  name: 'CommentList',
  components: {
    CreateComment,
  },
  data: function () {
    return {
      updateTrigger: false,
      updateCommentItem: null,
    }
  },
  props: {
    board: [Object, String],
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
    deleteComment: function (comment) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/${this.board.id}/comment/${comment.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          const targetCommentIdx = this.comments.findIndex((comment) => {
            return comment.id === res.data.id
          })
          this.$store.state.comments.splice(targetCommentIdx, 1)
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateBoard: function (comment) {
      this.updateTrigger = comment.id
      this.updateCommentItem = comment
    },
    changeTrigger: function () {
        this.updateTrigger = false
    }
  },
  created: function () {
    
  },
  computed: {
    ...mapState([
      'login',
      'login_user',
      'username',
      'is_admin',
      'comments',
    ])
  }
}
</script>

<style scoped>

</style>
