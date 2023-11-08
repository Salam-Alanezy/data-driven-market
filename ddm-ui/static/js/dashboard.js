
      document.addEventListener("DOMContentLoaded", function() {
          var accountChartCanvas = document.getElementById("account-chart");
          var accountChart = new Chart(accountChartCanvas, {
              type: "doughnut",
              data: {
                  labels: { expiring_products_count.keys() | list | tojson },
                  datasets: [{
                      data: { expiring_products_count.values() | list | tojson },
                      backgroundColor: ["#4e73df", "#1cc88a", "#36b9cc"],
                      borderColor: ["rgba(0,0,0,0.1)", "rgba(0,0,0,0.1)", "rgba(0,0,0,0.1)"]
                  }]
              },
              options: {
                  maintainAspectRatio: false,
                  legend: {
                    display: false,
                    labels: {
                      fontStyle: "normal"
                    }
                  },
                  title: {
                    fontStyle: "normal"
                  }
              }
          })
      })
