<template>
  <div>
    <h1 v-if="this.purpose == 'create'">글 작성</h1>
    <h1 v-else-if="this.purpose == 'update'">글 수정</h1>
    <div class="container">

      <form v-if="this.purpose == 'create'" v-on:submit.prevent="createBoard"
      class="font-poor font-1-2em">
        <div class="form-group row">
          <label class="col-sm-3 col-form-label" for="title">제목: </label>
          <div class="col-sm-9">
            <input type="text" class="form-control" id="title" v-model.trim="title">
          </div>
        </div>

        <div class="form-group row">
          <label for="content" class="col-sm-3 col-form-label">내용: </label>
          <div class="col-sm-9">
          <textarea class="form-control" id="content" v-model="content"></textarea>
          </div>
        </div>
        <button type="submit" class="btn btn-primary mt-3 font-1-5em btn-block">등록하기</button>
      </form>

      <form v-if="this.purpose == 'update'" v-on:submit.prevent="updateBoard">
        <div>
          <label for="title">제목: </label>
          <input type="text" id="title" v-model.trim="title">
        </div>
        <div>
          <label for="content">내용: </label>
          <input type="text" id="content" v-model="content">
        </div>
        <button type="submit" class="btn btn-primary mt-3 font-1-5em btn-block">등록하기</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'Board',
  data: function () {
    return {
      boards: [],
      title: null,
      content: null,
      updateId: null,
      purpose: null,
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
      const boardItem = {
        title: this.title,
        content: this.content,
      }

      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/board_create/',
        data: boardItem,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.$router.push({
            name: 'Board',
            params: {
              'id': res.data.id
            }
          })
        })
        .catch(err => {
          console.log(err)

        })
    },
    updateBoard: function () {
      const boardItem = {
        title: this.title,
        content: this.content,
        board_code: 1,
      }
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/community/board_update_delete/${this.updateId}/`,
        data: boardItem,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.$router.push({
            name: 'BoardDetail',
            params: {
              'id': res.data.id
            }
          })
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  created: function () {
    this.purpose = this.$route.params.purpose
    this.updateId = this.$route.params.id
    this.title = this.$route.params.title
    this.content = this.$route.params.content
  }
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

</style>