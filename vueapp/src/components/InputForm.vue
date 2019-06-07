<template>
  <v-form v-model="valid">
    <v-container>
      <v-layout>
        <v-flex
          xs12
          md4
        >
          <v-text-field
            v-model="name"
            :counter="30"
            label="게임을 입력하세요"
            required
          ></v-text-field>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>
</template>
<script>
  export default {
    data: () => ({
      valid: false,
      name: '',
    }),
    created() {
        this.$EventBus
    },
    watch: {
        name: function (name) {
            this.$EventBus.$emit('game-name-pass', this.name)
        }
    }
  }

</script>