<template>
    <div class="review-competition-list">
      <el-table :data="competitionList" stripe style="width: 100%">
        <el-table-column prop="competitionName" label="竞赛名称" width="200"></el-table-column>
        <el-table-column prop="submissionDate" label="提交日期" width="180"></el-table-column>
        <el-table-column prop="submittedBy" label="提交者" width="150"></el-table-column>
        <el-table-column prop="status" label="状态" width="120">
          <template #default="scope">
            <el-tag :type="getTagType(scope.row.status)">
              {{ scope.row.status }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="200">
          <template #default="scope">
            <el-button size="small" type="primary" @click="approveCompetition(scope.row.id)">通过</el-button>
            <el-button size="small" type="danger" @click="rejectCompetition(scope.row.id)">驳回</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { ElMessage } from 'element-plus';
  
  export default {
    name: 'ReviewCompetitionList',
    setup() {
      const competitionList = ref([]);
  
      const fetchCompetitionList = async () => {
        // Fetch pending competitions from the backend
        try {
          const response = await fetch('/api/competitions/pending');
          const data = await response.json();
          competitionList.value = data;
        } catch (error) {
          ElMessage.error('获取竞赛信息失败');
        }
      };
  
      const approveCompetition = async (id) => {
        // Send approval request to backend
        try {
          await fetch(`/api/competitions/${id}/approve`, { method: 'POST' });
          ElMessage.success('竞赛已通过');
          fetchCompetitionList();
        } catch (error) {
          ElMessage.error('操作失败');
        }
      };
  
      const rejectCompetition = async (id) => {
        // Send rejection request to backend
        try {
          await fetch(`/api/competitions/${id}/reject`, { method: 'POST' });
          ElMessage.success('竞赛已驳回');
          fetchCompetitionList();
        } catch (error) {
          ElMessage.error('操作失败');
        }
      };
  
      const getTagType = (status) => {
        return status === '待审核' ? 'warning' : 'success';
      };
  
      onMounted(fetchCompetitionList);
  
      return { competitionList, approveCompetition, rejectCompetition, getTagType };
    },
  };
  </script>
  
  <style scoped>
  .review-competition-list {
    padding: 20px;
  }
  </style>