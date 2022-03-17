<template>
  <div class="posts">
    <NavBar></NavBar>
      <div class="album py-5 bg-light">
          <div class="container">
            <div class="row">
              <div v-for="posts in APIData" :key="posts.id" class="col-md-4">
                <div class="card mb-4 box-shadow">
                  <div class="card-body">
                      <h4 class=""><div class="text-secondary" href="">{{posts.service}} for {{posts.client}}</div></h4>
                      <p class="card-text">{{posts.price}}</p>
                      <div class="d-flex justify-content-between align-items-center">
                      <div class="btn-group">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
  </div>
</template>


<script>
  import $ from 'jquery'
  import NavBar from '../components/Navbar'
  export default {
    name: 'applications',
    components: {
      NavBar
    },
    created () {
        this.getObj()
    },
    data () {
      return {
        APIData: ""
      }
    },
    methods: {

      /**
        * Get all services
        * 
        * @returns {List<Object>} - list of worker objects
        */
      getObj () {
      $.ajax({
        url: 'http://127.0.0.1:8000/api/applications',
        type: 'GET',
        success: (response) => {
          console.log(response)
          this.APIData = response
        },
        error: (response) => {
          console.log(response)
        }
      })
    }
    }
  }
</script>