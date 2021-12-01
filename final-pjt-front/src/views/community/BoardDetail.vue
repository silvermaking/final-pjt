<template>
  <div class="container">
    <div class="row">
      <h1 class="my-5">글 상세보기</h1>
    </div>
    <div class="row d-flex font-poor">
      <div class="media" style="width: 100%; word-break:break-all;">
        <div class="media-body text-justify">
          <h2 class="mt-0">{{board.title}}</h2>
          <p>작성자: {{boardUsername}}</p>
          <p>작성일: {{ $moment(board.created_at).format('YYYY-MM-DD hh:mm:ss') }} |
            수정일: {{ $moment(board.updated_at).format('YYYY-MM-DD hh:mm:ss') }}</p>
          <p class="font-2em">
            {{board.content}}
          </p>
          <hr :style="{'margin':'5px 30px'}">
          <hr :style="{'margin':'5px 30px'}">
          <div class="d-flex justify-content-end">
            <button class="btn btn-warning font-do mr-3 font-1-2em"
              v-if="boardUsername === this.$store.state.username"
              @click="updateBoard(board)">글 수정</button>
            <button class="btn btn-danger font-do mr-3 font-1-2em"
              v-if="this.$store.state.is_admin"
              @click="deleteBoard(board)">글 삭제</button>
            <button class="btn btn-danger font-do mr-3 font-1-2em"
              v-else-if="boardUsername === this.$store.state.username"
              @click="deleteBoard(board)">글 삭제</button>
          </div>
        <div>
          <hr>
          <hr>
          <div>
            <button @click="backToBoard" class="btn">게시글 목록</button>
          </div>
          <div class="mt-5">
            <CommentForm v-if="this.$store.state.login" :board="board" />
            <p v-else>댓글을 작성하려면 로그인이 필요합니다. </p>
          </div>
          <hr :style="{'margin':'5px 30px'}">
          <CommentList :board="board" />
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
import CommentForm from '@/components/CommentForm.vue'
import axios from 'axios'

export default {
  name: 'MovieDetail',
  components: {
    CommentList,
    CommentForm,
  },
  data: function () {
    return {
      board: null,
      boardUsername: null,
      boardItem: null,
      all_comments: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    backToBoard: function () {
      this.$router.push({
        name: 'Board'
      })
    },
    deleteBoard: function (board) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/community/board_update_delete/${board.id}/`,
        headers: this.setToken()
      })
        .then(() => {
          this.$router.push({
            name: 'Board'
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateBoard: function (board) {
      const boardItem = {
        id: board.id,
        purpose: 'update',
        title: board.title,
        content: board.content
      }
      this.$router.push({
        name: 'CreateBoard',
        params: boardItem
      })
    },
    getAllComment: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/${this.boardId}/comments/`,
        headers: this.setToken()
      })
        .then(res => {
          if (res.data) {
            this.$store.state.comments = res.data
            this.all_comments = this.$store.state.comments
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.boardItem = this.$route.params.id
    // console.log(this.boardItem)
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/community/${this.boardItem}/`,
      headers: this.setToken()
    })
      .then(res => {
        this.board = res.data
        // console.log(this.board)
        this.boardUsername = this.board.user.username
      })
      .catch(err => {
        console.log(err)
      })
    this.getAllComment()
  },
}
</script>

<style scoped>

</style>