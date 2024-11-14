
<template>
  <el-table :data="competitions" stripe>
    <el-table-column prop="name" label="竞赛名称" width="180"></el-table-column>
    <el-table-column prop="category" label="类别" width="120"></el-table-column>
    <el-table-column prop="instructor" label="指导老师" width="150"></el-table-column>
    <el-table-column prop="awardTime" label="获奖时间" width="150"></el-table-column>
    <el-table-column label="操作">
      <template #default="scope">
        <el-button @click="viewDetails(scope.row)">查看详情</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      competitions: [],
    };
  },
  created() {
    axios.get('/api/competitions').then(response => {
      this.competitions = response.data;
    });
  },
  methods: {
    viewDetails(competition) {
      // 打开详细信息或跳转到详情页面
    },
  },
};
</script>