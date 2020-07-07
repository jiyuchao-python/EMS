<template>
		<div id="wrap">
			<div id="top_content">
					<div id="header">
						<div id="rightheader">
							<p>2020/07/04<br /></p>
						</div>
						<div id="topheader">
							<h1 id="title"><a href="#">Main</a></h1>
						</div>
						<div id="navigation">
						</div>
					</div>
				<div id="content">
					<p id="whereami"></p>
					<h1>更新员工信息:</h1>
<!--					<form action="emplist.html" method="post">-->
						<table cellpadding="0" cellspacing="0" border="0"
							class="form_table">
							<tr>
								<td valign="middle" align="right">ID:</td>
								<td valign="middle" align="left">{{$route.params.id}}</td>
							</tr>
							<tr>
								<td valign="middle" align="right">姓名:</td>
								<td valign="middle" align="left"><input type="text" class="inputgri" name="name" v-model="username"></td>
							</tr>
							<tr>
								<td valign="middle" align="right">头像:</td>
								<td valign="middle" align="left"><input type="file" name="photo"ref="head_pic" /></td>
							</tr>
							<tr>
								<td valign="middle" align="right">工资:</td>
								<td valign="middle" align="left"><input type="text" class="inputgri" name="salary" v-model="salary"/></td>
							</tr>
							<tr>
								<td valign="middle" align="right">年龄:</td>
								<td valign="middle" align="left"><input type="text" class="inputgri" name="age"v-model="age" /></td>
							</tr>
						</table>
						<p>
<!--							<input type="submit" class="button" value="提交" />-->
              <button @click="update()">提交</button>
						</p>
<!--					</form>-->
				</div>
			</div>
			<div id="footer">
				<div id="footer_bg">
					ABC@126.com
				</div>
			</div>
		</div>
</template>

<script>
    export default {
      name: "Update_emp",
      data(){
        return{
          id:"",
          username:"",
          head_pic:"",
          salary:"",
          age:"",
          emp:{},
        }
      },
      methods:{
        get_id(){
          let emp_id=this.$route.params.id;
          // alert(emp_id),
          this.$axios.get("http://127.0.0.1:8000/api/emp/"+ emp_id +"/").then(res=>{
            console.log(res.data)
            this.emp=res.data;
          }).catch(error=>{
            console.log(error);
            this.$message.error("错误错误！")
          })
        },
        update(){
          console.log(this.$refs.head_pic.files[0]);
          let formData = new FormData();
          formData.append("emp_name", this.username);
          formData.append("head_pic", this.$refs.head_pic.files[0]);
          formData.append("salary", this.salary);
          formData.append("age", this.age);
          this.$axios({
              url:"http://127.0.0.1:8000/api/emp/"+ `${this.$route.params.id}` +`/`,
              method:"put",
              data:formData,
              headers:{
              'content-type': 'multipart/form-data'
          },
          }).then(res=>{
            console.log(res.data);
            this.$router.push("/Index");
          }).catch(error=>{
            this.$message.error("添加失败！")
          })
        },
      },
      created() {
        this.get_id()
      },
    }
</script>

<style scoped>

</style>
