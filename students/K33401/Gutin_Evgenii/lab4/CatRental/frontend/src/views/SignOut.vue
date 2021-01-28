<script>
export default {
  name: 'SignOut',
  created () {
    localStorage.removeItem('token')
    this.$router.push('/')
  }
}
</script>
