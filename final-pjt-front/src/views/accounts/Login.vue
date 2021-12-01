<template>
  <div class="login-cover">
    <div class="login-card pb-1">

    <h1>Login</h1>
    <div class="form-group mt-3 font-poor font-1-2em">
      <label for="username">사용자 이름: </label>
      <input type="text"
        id="username"
        v-model="credentials.username"
      >
    </div>
    <div class="form-group mt-3 font-poor font-1-2em">
      <label for="password">비밀번호: </label>
      <input type="password"
        id="password"
        v-model="credentials.password"
        @keyup.enter="login"
      >
    </div>
    <div>
      <button @click="login" id="login-button" class="btn btn-primary mt-3 font-1-5em btn-block">로그인</button>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('changeLogin')
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err)
          alert("로그인 정보를 다시 확인해주세요.")
        })
    }
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

.login-cover {
  position: relative;
  z-index: 3;
  width: 100vw;
  height: 100vh;
  background-color: black;
}

.container {
  padding: 16px;
}

.login {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

#login-button {
  width: 100%;
  margin-top: 40px;
  padding: 14px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  transition: 0.5s;
  font-size: 16px;
  color: #ffffffd1;
}

.login-card{
  background-color: rgba(0, 0, 0, 0.9);
  border-color: rgba(0, 0, 0, 0.9);
}

.login-form {
  width: 290px;
}

form {
  border: 2px solid #52B882;
  padding: 8px;
  border-radius: 2px;
}

form:focus-within {
  background: #7CF0BD;
}

label {
  display: inline-block;
  width: 72px;
}

input {
  margin: 4px 12px;
}

</style>