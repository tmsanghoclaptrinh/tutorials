// Đề bài: https://www.spoj.com/SPOJ/problems/HVT_QV/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_M = 1000;
const int MAX_N = 1000;

int M, N;
int height[MAX_M][MAX_N];
bool visited[MAX_M][MAX_N];

// Hướng di chuyển: phải, xuống, trái, lên
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};

// Kiểm tra xem ô (i, j) có nằm ngoài giới hạn ma trận không
bool isOutOfBounds(int i, int j)
{
    return (i < 0 || i >= M || j < 0 || j >= N);
}

// Kiểm tra xem ô (i, j) có phải là một phần của khối nhà chưa được thăm không
bool isUnvisitedBuilding(int i, int j)
{
    return (!visited[i][j] && height[i][j] > 0);
}

// Kiểm tra xem ô (i, j) có nằm ngoài giới hạn ma trận hoặc là ô trống không
bool isBoundaryOrEmpty(int i, int j)
{
    return isOutOfBounds(i, j) || height[i][j] == 0;
}

// Kiểm tra xem chiều cao của ô lân cận (i, j) có nhỏ hơn chiều cao của ô hiện tại không
bool isLowerBuilding(int i, int j, int currentHeight)
{
    return height[i][j] < currentHeight;
}

// Hàm loang để tìm và tính toán diện tích quét vôi của khối nhà bắt đầu từ ô (i, j)
int floodFill(int i, int j)
{
    // Nếu ô (i, j) nằm ngoài giới hạn hoặc đã được thăm, hoặc là ô trống, thì dừng lại
    if (isOutOfBounds(i, j) || visited[i][j] || height[i][j] == 0)
    {
        return 0;
    }

    visited[i][j] = true;
    int area = 0;      // Diện tích khối nhà
    int perimeter = 0; // Diện tích quét vôi

    // Duyệt qua 4 hướng (phải, xuống, trái, lên)
    for (int dir = 0; dir < 4; dir++)
    {
        int neighbor_i = i + dx[dir];
        int neighbor_j = j + dy[dir];

        // Nếu là biên hoặc ô trống
        if (isBoundaryOrEmpty(neighbor_i, neighbor_j))
        {
            perimeter += height[i][j];
        }
        // Nếu ô lân cận có chiều cao thấp hơn, cộng thêm phần chênh lệch chiều cao
        else if (height[neighbor_i][neighbor_j] != 0 && isLowerBuilding(neighbor_i, neighbor_j, height[i][j]))
        {
            perimeter += (height[i][j] - height[neighbor_i][neighbor_j]);
        }

        // Đệ quy để mở rộng khối nhà
        area += floodFill(neighbor_i, neighbor_j);
    }

    return perimeter + area;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> M >> N;

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> height[i][j];
            visited[i][j] = false;
        }
    }

    int numberOfBuildings = 0;    // Số lượng khối nhà
    long long totalPerimeter = 0; // Tổng diện tích quét vôi
    long long maxPerimeter = 0;   // Diện tích quét vôi lớn nhất
    int maxBuildingID = -1;       // ID khối nhà có diện tích quét vôi lớn nhất

    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < N; j++)
        {
            // Nếu phát hiện 1 khối nhà chưa được thăm
            if (isUnvisitedBuilding(i, j))
            {
                numberOfBuildings++;
                long long currentPerimeter = floodFill(i, j); // Tính diện tích quét vôi của khối nhà hiện tại
                totalPerimeter += currentPerimeter;           // Cộng vào tổng diện tích quét vôi

                // Cập nhật khối nhà có diện tích quét vôi lớn nhất
                if (currentPerimeter > maxPerimeter)
                {
                    maxPerimeter = currentPerimeter;
                    maxBuildingID = numberOfBuildings;
                }
            }
        }
    }

    cout << numberOfBuildings << '\n';
    cout << totalPerimeter << '\n';
    cout << maxBuildingID << ' ' << maxPerimeter;

    return 0;
}
