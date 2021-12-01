<template>
  <div class="signup-cover">
    <div class="signup-card pb-1">

    <h1>Signup</h1>
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
      >
    </div>
    <div class="form-group mt-3 font-poor font-1-2em">
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password"
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
        @keyup.enter="signup"
      >
    </div>
    <div class="form-group mt-3 font-poor font-1-2em">
      <label for="date_of_birth">생년월일: </label>
      <input type="date"
        id="date_of_birth"
        v-model="credentials.date_of_birth"
      >
    </div>
    <div class="form-group mt-3 font-poor font-1-2em">
      <label for="email">이메일: </label>
      <input type="email"
        id="email"
        v-model="credentials.email"
        @keyup.enter="signup"
      >
    </div>
    <button @click="signup" id="signup-button" class="btn btn-primary mt-3 font-1-5em btn-block">회원가입</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Singup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
        date_of_birth: null,
        email: null,
      },
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
          alert("회원가입 정보를 다시 확인해주세요.")
        })
    }
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

.signup-cover {
  position: relative;
  z-index: 3;
  width: 100vw;
  height: 100vh;
  background-color: black;
}

.container {
  padding: 16px;
}
.signup {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

#signup-button {
  width: 100%;
  margin-top: 40px;
  padding: 14px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  transition: 0.5s;
  font-size: 16px;
  color: rgba(255, 255, 255, 0.82);
}
.signup-card{
  background-color: rgba(0, 0, 0, 0.9);
  border-color: rgba(0, 0, 0, 0.9);
}

.signup-form {
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