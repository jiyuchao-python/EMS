<template>
		<div id="wrap">
			<div id="top_content">
				<div id="header">
					<div id="rightheader">
						<p>2020/07/04<br /> <a href="" @click="quit">安全退出</a></p>
					</div>
					<div id="topheader">
						<h1 id="title">
							<a href="#">main</a>
						</h1>
					</div>
					<div id="navigation">
					</div>
				</div>
				<div id="content">
					<p id="whereami"></p>
					<h1>欢迎~{{user_message}}~访问百知教育</h1>
					<table class="table">
						<tr class="table_header">
							<td>ID</td>
							<td>Name</td>
							<td>Photo</td>
							<td>Salary</td>
							<td>Age</td>
							<td>Operation</td>
						</tr>
						<tr v-for="(emp,index) in emp_list" :key="emp.id">
							<td>{{emp.id}}</td>
							<td>{{emp.emp_name}}</td>
              <td><img :src="emp.img"style="height: 60px;"></td>
							<td>{{emp.salary}}</td>
							<td>{{emp.age}}</td>
              <td>
                <router-link :to="`/Update_emp/`+emp.id">修改</router-link>&nbsp
                <a href="" @click="dele(emp.id)">删除</a>&nbsp;
              </td>
						</tr>
					</table>
					<p>
<!--						<input type="button" class="button" value="添加员工"/>-->
            <button> <router-link to="/Add_emp">添加员工</router-link></button>
					</p>
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
        name: "Index",
        methods:{
          quit(){
            sessionStorage.clear()
          },
          select_all(){
              this.$axios.get("http://127.0.0.1:8000/api/emp/").then(res=>{
                console.log(res.data.results);
                this.emp_list=res.data.results
            }).catch(error=>{
              console.log(error);
              this.$message.error("查询失败！")
            })
          },
          dele(id){
            console.log(id)
            // console.log(${id})
            this.$axios.delete("http://127.0.0.1:8000/api/emp/"+id+"/").then(res=>{
              // alert('成功！');
              this.$router.go(0)
              // this.$router.push("/Index")
            }).catch(error=>{
              console.log(error);
              // alert('失败！');
              this.$message.error("删除失败！")
            })
             // this.$router.push("/Index")
          },
        },
        data(){
          return{
            user_message:"",
            emp_list:[],
          }
        },
        created() {
            let login_flag=sessionStorage["username"];
            console.log(login_flag)
            this.user_message=login_flag
            if (login_flag){
              this.$message.success("百知教育欢迎你！")
            }
            else {
              this.$message.error("请登录！")
              this.$router.push("/login")
            }
            this.select_all()
        }
    }
</script>

<style scoped>

</style>
