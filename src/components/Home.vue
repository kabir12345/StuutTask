<script setup lang="ts">
import { onMounted, ref } from 'vue'
import api from '@/api'


const ticker = ref('')
const stock = ref(null)

const searchStock = async () => {
  try {
    const response = await api.get(`/stock?ticker=${ticker.value}`)
    stock.value = response.data
  } catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  try {
    const response = await api.get('/welcome')
    welcomeMessage.value = response.data.message
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div>
    <input v-model="ticker" placeholder="Enter stock ticker">
    <button @click="searchStock">Search</button>
    <div v-if="stock">
      <h1>{{ stock.longName }}</h1>
      <table>
        <tr>
          <th>Address</th>
          <td>{{ stock.address1 }}, {{ stock.city }}, {{ stock.state }}, {{ stock.zip }}, {{ stock.country }}</td>
        </tr>
        <tr>
          <th>Phone</th>
          <td>{{ stock.phone }}</td>
        </tr>
        <tr>
          <th>Website</th>
          <td><a :href="stock.website" target="_blank">{{ stock.website }}</a></td>
        </tr>
        <tr>
          <th>Industry</th>
          <td>{{ stock.industry }}</td>
        </tr>
        <tr>
          <th>Sector</th>
          <td>{{ stock.sector }}</td>
        </tr>
        <tr>
          <th>Business Summary</th>
          <td>{{ stock.longBusinessSummary }}</td>
        </tr>
        <tr>
          <th>Full-Time Employees</th>
          <td>{{ stock.fullTimeEmployees }}</td>
        </tr>

        <tr>
          <th>Current Price</th>
          <td>{{ stock.currentPrice }}</td>
        </tr>
        <tr>
          <th>52 Week High</th>
          <td>{{ stock.fiftyTwoWeekHigh }}</td>
        </tr>
        <tr>
          <th>52 Week Low</th>
          <td>{{ stock.fiftyTwoWeekLow }}</td>
        </tr>
        <tr>
          <th>Market Cap</th>
          <td>{{ stock.marketCap }}</td>
        </tr>
        <tr>
          <th>PE Ratio</th>
          <td>{{ stock.trailingPE }}</td>
        </tr>
        <tr>
          <th>Dividend Rate</th>
          <td>{{ stock.dividendRate }}</td>
        </tr>
        <tr>
          <th>Dividend Yield</th>
          <td>{{ stock.dividendYield }}</td>
        </tr>
        <tr>
          <th>Beta</th>
          <td>{{ stock.beta }}</td>
        </tr>
        <tr>
          <th>Average Volume</th>
          <td>{{ stock.averageVolume }}</td>
        </tr>
        <tr>
          <th>Volume</th>
          <td>{{ stock.volume }}</td>
        </tr>
        <tr>
          <th>Total Revenue</th>
          <td>{{ stock.totalRevenue }}</td>
        </tr>
        <tr>
          <th>EBITDA</th>
          <td>{{ stock.ebitda }}</td>
        </tr>
        <tr>
          <th>Net Income</th>
          <td>{{ stock.netIncomeToCommon }}</td>
        </tr>
        <tr>
          <th>Operating Cashflow</th>
          <td>{{ stock.operatingCashflow }}</td>
        </tr>
        <tr>
          <th>Free Cashflow</th>
          <td>{{ stock.freeCashflow }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<style>
input{
  width:100%;
  height:50px;
  border-radius: 5%;
}
h1{
  color:white;
  font-weight: bolder;
}
button{
  color: #01BD7E;
  background-color: #181818 !important;
  border: 1px #01BD7E !important;
  border-radius: 2px;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  color: white;
}

th {
  text-align: left;
}
</style>
