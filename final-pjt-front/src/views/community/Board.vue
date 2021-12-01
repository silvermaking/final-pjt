<template>
  <div>
    <div class="container">
    <div class="row">
      <div class="font-do my-3">
        <h1>게시판</h1>
      </div>
      <div class="btn btn-blue font-1-5em my-4">
        <button @click="createBoard()" id="board-button" class="btn btn-primary mt-3 font-1-5em btn-block">글쓰기</button>
      </div>
    </div>
    <div>
      <table class="table">
        <tr>
          <th>No</th>
          <th>제목</th>
          <th>작성자</th>
          <th>작성일</th>
            <td></td>
        </tr>
        <tr v-for="(board,idx) in boards" :key="idx">
            <th>{{ board.id }}</th>
            <th @click="boardDetail(board)">{{ board.title }}</th>
            <th>{{ board.user.username }}</th>
            <th>{{ $moment(board.created_at).format('YYYY-MM-DD hh:mm:ss') }}</th>
          </tr>
      </table>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import Comment from '@/components/Comment.vue'

  export default {
    name: 'Board',
    data: function () {
      return {
        boards: [],
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
      createBoard: function () {
        this.$router.push({
          name: 'CreateBoard',
          params: {
            'purpose': 'create'
          }
        })
      },
      boardDetail: function (board) {
        this.$router.push({
          name: 'BoardDetail',
          params: {
            'id': board.id
          }
        })
      }
    },
    created: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/community/`,
        headers: this.setToken(),
      })
        .then(res => {
          this.boards = res.data
          console.log(this.boards)
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
</script>

<style scoped>
#bg {
  position: fixed; 
  z-index: -1;
  top: 0; 
  left: 0; 
  margin: auto;
}

.board-cover {
  position: fixed;
  z-index: 3;
  width: 100vw;
  height: 100vh;
  background-color: black;
}

.container {
  padding: 16px;
}

.board {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

#board-button {
  width: 10%;
  margin-top: 40px;
  padding: 14px 20px;
  border: none;
  cursor: pointer;
  width: 10%;
  transition: 0.5s;
  font-size: 16px;
  color: rgba(255, 255, 255, 0.82);
}
.board-card{
  background-color: rgba(0, 0, 0, 0.9);
  border-color: rgba(0, 0, 0, 0.9);
}

.board-form {
  width: 290px;
}

.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
  background-image: linear-gradient(
      45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    ),
    linear-gradient(
      -45deg,
      #000 25%,
      transparent 25%,
      transparent 75%,
      #000 75%,
      #000
    );
  background-size: 60px 60px;
  background-repeat: repeat;
}
</style>
