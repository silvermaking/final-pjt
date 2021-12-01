<template>
  <div id="app">
    <nav id="nav" class="navbar justify-content-end sticky-top navbar-dark bg-dark">
      <span v-if="isLogin">
        <div class="container-fluid">
          <a class="navbar-brand d-flex flex-row-reverse bd-highlight mb-3" href="/">SSAFLIX</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="offcanvasNavbarLabel">SSAFLIX</h5>
              <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
          <div class="offcanvas-body">
            <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page">
                <router-link to="/">Home</router-link></a>
              </li>
              <li class="nav-item">
                <a class="nav-link">
                <router-link to="/random">Recommend</router-link></a>
              </li>
              <!-- <li class="nav-item">
                <a class="nav-link">
                <router-link to="/movies/movie-list">MovieList</router-link></a>
              </li> -->
              <li class="nav-item">
                <a class="nav-link">
                <router-link to="/community/board">Board</router-link></a>
              </li>
              <li class="nav-item">
                <a class="nav-link">
                <router-link to="#" @click.native="logout">Logout</router-link></a>
              </li>
            </ul>
        <form class="d-flex">
          <input class="me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-primary" type="submit">Search</button>
        </form>
          </div>
        </div>
      </div>
      </span>
      <span v-else>
        <router-link to="/">Home</router-link> |
        <router-link to="/accounts/signup">Signup</router-link> |
        <router-link to="/accounts/login">Login</router-link>
      </span>

    </nav>
    <router-view @changeLogin="changeLogin"/>
  </div>
</template>

<script>
// import Login from '@vue/accounts/Login.vue'

export default {
  name: 'App',
  data: function() {
    return {
      isLogin: false
    }
  },
  methods: {
    changeLogin: function () {
      this.isLogin = true
    },
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>


<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #546a80;
  margin: 0;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

body {
  margin: 0;
  padding: 0;
  background: #3d84c7;
  background-size: contain;
}

#nav {
  padding: 20px;
}

#nav a {
  font-weight: bold;
  color: #237bce;
}

#nav a.router-link-exact-active {
  color: #1b399b;
}

.left{
  float: left;
}

.right{
  float: right;
}

</style>
