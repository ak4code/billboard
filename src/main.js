import Vue from 'vue'
import UIkit from 'uikit'
import '@/assets/styles/styles.scss'
import Icons from 'uikit/dist/js/uikit-icons'

Vue.config.productionTip = false

UIkit.use(Icons)
window.UIkit = UIkit

new Vue({
  el: '#app',
  components: {}
})
