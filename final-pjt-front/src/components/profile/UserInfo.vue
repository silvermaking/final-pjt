<template>
  <div>
    <header id="header">
      <span class="avatar">
        <el-tooltip content="하이❤" placement="right" :offset="-40" effect="light">
          <a data-bs-toggle="modal" data-bs-target="#profileModal">
            <img v-if="image === SERVER_URL+'null'" src="@/assets/default_profile.jpg" alt=""/>
            <img v-else :src="image" alt="" />
          </a>
        </el-tooltip>
      </span>
      <h2 style="font-size: 30px;">{{ nickname }}님의 공간</h2>
    </header>

    <div class="modal fade p-0" id="profileModal" tabindex="-1" aria-labelledby="profileModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title fw-bold">프로필 편집</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="initModal"></button>
          </div>
          <el-form
            class="profile-form"
            :model="credentials"
            :rules="rules"
            ref="form"
            style="margin-top: 3rem; margin-left: 6.7rem;"
          >
            <el-form-item prop="nickname">
              <el-input v-model="credentials.newNickname" placeholder="닉네임" prefix-icon="fas fa-user"></el-input>
            </el-form-item>
            <el-form-item prop="image">
              <el-input
                @change.native='onGetFile'
                type="file"
                accept="image/*"
                v-model="credentials.newImage"
                placeholder="image"
                prefix-icon="el-icon-picture-outline"
                class="mt-2"
              ></el-input>
            </el-form-item>
            <el-form-item>
              <el-button
                id="profile-button"
                type="primary"
                native-type="submit"
                @click.native.prevent="sendImageToServer"
                block
                class="mb-2"
                data-bs-dismiss="modal"
              ><span style="color: rgba(255, 255, 255, 0.82);">변경</span></el-button>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import SERVER from '@/api/drf.js'
import swal from 'sweetalert'
export default {
  name: "UserInfo",
  data: function () {
    return {
      credentials: {
        newNickname: '',
        newImage: '',
      },
      rules: {
        newNickname: [
          {
            required: true,
            message: "Nickname is required",
            trigger: "blur"
          },
        ],
      },
      SERVER_URL: SERVER.URL,
    }
  },
  methods: {
    initModal: function () {
      this.credentials.newNickname = ''
      this.credentials.newImage = ''
    },
    onGetFile (event) {
      this.credentials.newImage = event.target.files[0]
    },
    sendImageToServer () {
      if (this.credentials.newNickname === '') {
        swal ("닉네임을 입력해주세요.", {
          dangerMode: true,
        })
      } else if (this.credentials.newImage === '') {
        swal ("이미지를 선택해주세요.", {
          dangerMode: true,
        })
      } else {
        const formData = new FormData()
        formData.append('image', this.credentials.newImage)
        formData.append('nickname', this.credentials.newNickname)
        this.profileUpdate(formData)
      }
    },
    ...mapActions([
      'profileUpdate',
    ])
  },
  computed: {
    ...mapState([
      'nickname',
      'image'
    ])
  },
}
</script>

<style>
#header {
  text-align: center;
  padding: 6em 0 3em 0;
}
h2 {
  color: rgba(255, 255, 255, 0.8);
  font-weight: 200;
}
.avatar {
  border-radius: 100%;
  display: inline-block;
  margin: 0 0 2em 0;
  padding: 0.5em;
  border: solid 1px rgba(255, 255, 255, 0.25);
  background-color: rgba(255, 255, 255, 0.075);
}
#header .avatar img {
  border-radius: 100%;
  display: block;
  width: 10em;
  cursor: pointer;
  transition: 0.3s;
}
.avatar img:hover {
  filter: brightness(1.2);
  transform: translateY(1.5px) rotate(-10deg);
}
@media screen and (max-width: 1280px) {
  #header {
    padding: 4em 0 2em 0;
  }
}
.modal-open { 
  padding-right: 0px !important;
}
.profile-form {
  width: 290px;
}
#profile-button {
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
</style>

<style lang="scss">
$teal: rgba(71, 63, 113, 0.8);
#profile-button {
  background: $teal;
  border-color: $teal;
  &:hover,
  &.active,
  &:focus {
    background: lighten($teal, 20);
    border-color: lighten($teal, 20);
  }
}
</style>