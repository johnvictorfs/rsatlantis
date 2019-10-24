<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" lg="8" md="10" sm="12">
        <v-card class="api-card mt-2" elevation="6">
          <v-toolbar class="text-center" color="#353434">
            <v-spacer></v-spacer>
            <v-toolbar-title>
              <h2 style="font-family: Rubik;">Documentação da API</h2>
            </v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>

          <v-tabs center-active v-model="tab" color="light-blue" background-color="deep-gray accent-4">
            <v-tabs-slider></v-tabs-slider>
            <v-tab href="#guides-api" ripple @click="updateBaseUrls">Guias</v-tab>
            <v-tab href="#users-api" ripple @click="updateBaseUrls">Usuários</v-tab>

            <v-tab-item value="guides-api">
              <div class="api-markdown">
                <Guide />
              </div>
            </v-tab-item>

            <v-tab-item value="users-api">
              <div class="api-markdown">
                <Users />
              </div>
            </v-tab-item>
          </v-tabs>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import Component from 'vue-class-component'

// @ts-ignore
import Guide from '@/assets/docs/api/guides.md'

// @ts-ignore
import Users from '@/assets/docs/api/users.md'

@Component({ components: { Guide, Users } })
export default class ApiDocs extends Vue {
  tab = null;

  mounted() {
    this.updateBaseUrls()
  }

  private updateBaseUrls() {
    /**
     * Replace all mentions of '{base_url}' in the markdown HTML to the
     * actual API's base url
     */
    setTimeout(() => {
      const apiElements = document.getElementsByClassName('api-markdown')

      for (let i = 0; i < apiElements.length; ++i) {
        apiElements[i].innerHTML = apiElements[i].innerHTML.replace(/{base_url}/g, process.env.VUE_APP_API_URL || '')
        apiElements[i].innerHTML = apiElements[i].innerHTML.replace(/✔️/g, '<i class="v-icon notranslate fa fa-check theme--dark"></i>')
        apiElements[i].innerHTML = apiElements[i].innerHTML.replace(/❌/g, '<i class="v-icon notranslate fa fa-times theme--dark"></i>')
      }
    }, 1000)
  }
}
</script>

<style lang="scss">

.api-card {
  border-radius: 25px !important;
}

.api-markdown {
  $dark-gray: rgb(100, 99, 99);
  $darker-gray: rgb(48, 47, 47);
  $even-darker-gray: rgb(32, 32, 32);
  $white-gray: #fafafa;
  $dark-light-gray: rgb(73, 72, 72);
  $light-gray: rgb(122, 121, 121);
  $table-border-radius: 20px;

  margin-top: 15px;
  margin-right: 18px;
  margin-left: 18px;

  font-family: Muli;

  hr {
    $hr-margin: 15px;
    border: none;
    height: 4px;
    background-color: $light-gray;
    margin-bottom: $hr-margin;
    margin-top: $hr-margin;
    width: 100%;
    background: linear-gradient(90deg,#1976d2,rgba(25,118,210,0));
    border-radius: 3px;
  }

  h1, h2, h3, h4, h5 {
    margin-bottom: 10px;
  }

  ul li {
    position: relative;
    padding-bottom: 10px;
  }

  ul {
    list-style: none;
  }

  ul li:before{
    content: '';
    position: absolute;
    border-right: 2px solid #757575;
    border-bottom: 2px solid #757575;
    width: 8px;
    height: 8px;
    top: calc(50% - 6px);
    left: -15px;
    transform: translateY(-50%) rotate(-45deg);
  }

  li > p:first-child {
    margin: 0;
  }

  ul ul,ul ol {
    margin-bottom: .4em;
  }

  .table-caption {
    text-align: center;
    font-weight: bold;
    font-size: 20px;
    padding-top: 7px;
    padding-bottom: 7px;
    background-color: $even-darker-gray;
    margin-top: 2px;
    border-top-left-radius: $table-border-radius;
    border-top-right-radius: $table-border-radius;
  }

  .table-success {
    background-color: rgb(39, 126, 39);
  }

  .table-error {
    background-color: rgb(179, 57, 57);
  }

  table {
    overflow: auto;
    margin-bottom: 20px;
    text-align: center;
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    width: 100%;
    empty-cells: hide;

    tbody {
      display: table-row-group;
      border-bottom-left-radius: $table-border-radius;
      border-bottom-right-radius: $table-border-radius;
    }

    td, th {
      /* border: 1px solid black; */
      padding: 8px;
      display: table-cell;
      font-family: Muli;
    }

    tr {
      td:nth-child(2) {
        font-family: 'Source Code Pro', Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
        color: lightskyblue;
      }
      background-color: $dark-light-gray;
    }

    tr:nth-child(even) {
      background-color: $dark-gray;
    }

    tr:hover {
      background-color: $light-gray;
    }

    tr:last-child {
      td:first-child {
        border-bottom-left-radius: $table-border-radius;
      }

      td:last-child {
        border-bottom-right-radius: $table-border-radius;
      }
    }

    th {
      padding-top: 12px;
      padding-bottom: 12px;
      background-color: $darker-gray;
      color: white;
    }
  }

  blockquote {
    background-color: rgb(100, 99, 99);
    border-left: 10px solid #ccc;
    margin: 1.5em 10px;
    padding: 0.5em 10px;
    border-radius: 10px;

    p {
      display: inline;
    }
  }

  blockquote:before {
    color: #ccc;
    font-size: 4em;
    line-height: 0.1em;
    margin-right: 0.25em;
    vertical-align: -0.4em;
  }

  :not(pre) > code {
    // Inline-code with ``
    font-family: 'Source Code Pro', Consolas, monospace;
    margin-left: 6px;
    border-radius: 8px;
    color: #d8dae4;
    background-color: rgb(100, 100, 100);
    border: 1px solid rgb(87, 87, 87);
  }

  :not(pre) > code:hover {
    background-color: rgb(88, 87, 87);
  }

  /**
   * PrismJS 1.17.1
   * https://prismjs.com/download.html#themes=prism-tomorrow&languages=clike+javascript+json+python
   * prism.js tomorrow night eighties for JavaScript, CoffeeScript, CSS and HTML
   * Based on https://github.com/chriskempson/tomorrow-theme
   * @author Rose Pritchard
   */
  code[class*="language-"],
  pre[class*="language-"] {
    color: #ccc;
    background: none;
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    font-size: 1em;
    text-align: left;
    white-space: pre;
    word-spacing: normal;
    word-break: normal;
    word-wrap: normal;
    line-height: 1.5;

    -moz-tab-size: 4;
    -o-tab-size: 4;
    tab-size: 4;

    -webkit-hyphens: none;
    -moz-hyphens: none;
    -ms-hyphens: none;
    hyphens: none;
  }

  /* Code blocks */
  pre[class*="language-"] {
    padding: 1em;
    margin: .5em 0;
    overflow: auto;
  }

  :not(pre) > code[class*="language-"],
  pre[class*="language-"] {
    background: #2d2d2d;
  }

  /* Inline code */
  :not(pre) > code[class*="language-"] {
    padding: .1em;
    border-radius: .3em;
    white-space: normal;
  }

  .hljs-comment,
  .hljs-block-comment,
  .hljs-prolog,
  .hljs-doctype,
  .hljs-cdata {
    color: #999;
  }

  .hljs-punctuation {
    color: #ccc;
  }

  .hljs-tag,
  .hljs-attr,
  .hljs-attr-name,
  .hljs-namespace,
  .hljs-deleted {
    color: #e2777a;
  }

  .hljs-function-name {
    color: #6196cc;
  }

  .hljs-boolean,
  .hljs-literal,
  .hljs-number,
  .hljs-function {
    color: #f08d49;
  }

  .hljs-property,
  .hljs-class-name,
  .hljs-constant,
  .hljs-symbol {
    color: #f8c555;
  }

  .hljs-selector,
  .hljs-important,
  .hljs-atrule,
  .hljs-keyword,
  .hljs-builtin {
    color: #cc99cd;
  }

  .hljs-string,
  .hljs-char,
  .hljs-attr-value,
  .hljs-regex,
  .hljs-variable {
    color: #7ec699;
  }

  .hljs-operator,
  .hljs-entity,
  .hljs-url {
    color: #67cdcc;
  }

  .hljs-important,
  .hljs-bold {
    font-weight: bold;
  }
  .hljs-italic {
    font-style: italic;
  }

  .hljs-entity {
    cursor: help;
  }

  .hljs-inserted {
    color: green;
  }
}
</style>
